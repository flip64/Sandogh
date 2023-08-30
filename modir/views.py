from django.shortcuts import render
from modir.models import *
from modir.forms  import taidemablagh
from django.views.decorators.csrf import csrf_exempt
from django.http  import HttpResponseRedirect ,HttpResponse
from modir.forms import taidemablagh
from django.views.generic.edit import CreateView # ne
from datetime import date
import calendar , datetime
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django_jalali.db import models as jmodels
import jdatetime  


#################################################  functins  

 #  test in ke agsate loan etmam yefteh ya na
def testEndLoan(l):
 list = Aghsat.objects.filter(loan = l) 
 for l in list:
   if (l.pardakht == None):
     return False
 return True


def next_month ( date ):
  """return a date one month in advance of 'date'.  
  If the next month has fewer days then the current date's month, this will return an
  early date in the following month."""
  return date + datetime.timedelta(days=calendar.monthrange(date.year,date.month)[1])


def bedehkariloan(member):
   bedhi = 0
   listLoans = Loan.objects.filter(member = member , state = True)
   for lo  in listLoans:
    listaghsat = Aghsat.objects.filter(loan = lo)
    for gest in listaghsat:
       if (gest.pardakht == None): 
        day = int((gest.tarikh - date.today()).days)
        if (day  < 0):
          bedhi = bedhi + gest.mablagh
   return (bedhi)


def bedehkariSandogh(member) : 
   bedhi = 0
   listaghsat = Zakhireh.objects.filter(member = member)
   for gest in listaghsat:
     if (gest.pardakht == None): 
        day = int((gest.doreh.tarikh- date.today()).days)
        if (day  < 0):
          bedhi = bedhi + gest.mablagh
   return (bedhi)


class memberByBedhi:
   def __init__(self, member, bedehiLoan ,bedehiSandogh):
    self.member = member
    self.bedehiLoan = bedehiLoan
    self.bedehiSandoh = bedehiSandogh


###################################################   viwe 


def index(request):
 listconfigh = ConfighDoreh.objects.all().order_by('titel')
 for configh in listconfigh:
  listdoreh = Doreh.objects.filter( configh = configh)
  if(len(listdoreh) == 0): 
    for n in range(1,13,1):
      if  n < 10 :
        z = str(0) + str(n)
      else :
        z = str(n)  
      
      
      da = jdatetime.date( year=int(configh.titel) , month=n, day = 1).togregorian()
      cdate = date.today()
      if(da < cdate ):
         doreh = Doreh(configh = configh , titel = configh.titel + z ,
                    tarikh = da)
         doreh.save()



 
 context = {
 
 
 }

 return render(request, "index.html", context)


def listMember(request):
    # list members by bedehkari hay khod
    list = []
    listMember = Member.objects.all()
    for m in listMember :
     list.append(memberByBedhi(m,bedehkariloan(m),bedehkariSandogh(m))  

    )   
    
    context = {
        'list' :  list,
        
    }

    return render(request, "members.html", context)

  
def creatDarkhastView(request, id):  
   aghsat = Aghsat.objects.get(id=id) 
   darkhast = Darkhast.objects.filter(Aghsat = aghsat)
   if(not bool(darkhast)):
     dis = "در خواست  پرداخت برای وام {} {} ارسال شد  ".format(aghsat.loan.member.user.first_name ,aghsat.loan.member.user.last_name)
     Darkhast.objects.create( 
     discription = dis ,
     acceptDate = None , 
     deletDate = None ,
     startDate = date.today(),
     Aghsat = aghsat 
            
   )

   return HttpResponseRedirect("/modir/listdarkhast/")


def creatDarkhastSandoghView(request,id):
   zakhireh = Zakhireh.objects.get(id= id)
   darkhastSanogh = DarkhastSandogh.objects.filter(Zakhireh = zakhireh)
   if(not bool(darkhastSanogh)):
      dis = "در خواست پرداخت صندوق برای {} ایجاد شد"
      DarkhastSandogh.objects.create(
         discription = dis,
         acceptDate = None , 
         deletDate = None , 
         startDate = date.today(), 
         Zakhireh = zakhireh 
      )
   return HttpResponseRedirect("/modir/listDarkhastPardakhtSandogh/")


def listLoans(request , id) :

      list = Loan.objects.filter(member_id= id , state= True)    
      if (len(list) != 0 ) : 
       state = list[0].state  
       member = Member.objects.filter(id=id)
       name = member.get().user.first_name + "  " +  member.get().user.last_name
       aghsatbaghmandel =  0
       
       context = {
        'list'    :  list ,
        'bagh'    :  aghsatbaghmandel,
        'name'    :  name , 
        'state'   :  state

       }
       return render(request, "loan.html", context)
      else:
        configh = {'title' :  'پرداخت وام'}  
        etebar = (Member.objects.filter(id=id).get().mablagh)  * 2.5 
        etebar = round(etebar)
        tform = taidemablagh
        context={
           'configpage' : configh,
           'etebr_vam' : etebar,
           'id' : id

        }
      return render(request, "pardakhtloan.html", context)


def listallLoans(request) :

      list = Loan.objects.all()
      print(len(list))
      context = {
        'list' :  list ,
      }
      return render(request, "loans.html", context)
            

def listaghsat(request , id) :

    loan = Loan.objects.filter(id=id)
    name = loan.get().member.user.first_name + "  " +  loan.get().member.user.last_name
    list = Aghsat.objects.filter(loan_id= id)
    context = {
        'list' :  list         
    }
    return render(request, "listaghsat.html", context)


class pardakhtloan(CreateView):
  model = Loan
  template_name = "createloan.html"
  fields = ['mablagh','tarikh','type','member']
  success_url = "/modir/members/"
  
  def form_valid(self, form):
     # This method is called when valid form data has been POSTed.
     # It should return an HttpResponse.
     mablaghLoan = form.cleaned_data['mablagh'] 
     tarikhLoan = form.cleaned_data['tarikh']
     typeLoan =  form.cleaned_data['type']
     memberLoan = form.cleaned_data['member']

     loan = Loan.objects.create(mablagh = mablaghLoan,tarikh = tarikhLoan , type = typeLoan , member = memberLoan)     
     tarikhAghsat = loan.tarikh
     count = typeLoan.tedadAghsat+1
     for x in range(1,count):
        type = form.cleaned_data['type']
        mablagh = form.cleaned_data['mablagh'] / type.tedadAghsat
        mablagh = round(mablagh) 
        tarikhAghsat = next_month(tarikhAghsat)
        pardakht  =  None
        shomareh = x
        Aghsat.objects.create(loan = loan,mablagh = mablagh , tarikh = tarikhAghsat , pardakht = pardakht , shomareh = shomareh)
           
     mojodi = MSandogh.objects.get()
     mojodi.mojodi -= mablaghLoan 
     mojodi.save()
      

     
     return HttpResponseRedirect('/modir/') 


class listDarkhastviwe(ListView):
    model = Darkhast 
    template_name = "list_darkhast.html"


class listDarkhastPardakhtSandoghViwe(ListView):
    model = DarkhastSandogh
    template_name = "list_darkhast_sandogh.html"
    

def taideDarkhastViwe(request , id):
 darkhast = Darkhast.objects.get(id = id)
 darkhast.acceptDate = datetime.date.today()
 aghsat = darkhast.Aghsat
 aghsat.pardakht = datetime.date.today()
 aghsat.save()
 darkhast.save()
  
  ###  افزایش موجودی صندوق 
 mojodi = MSandogh.objects.get()
 mojodi.mojodi += aghsat.mablagh 
 mojodi.save()
 
 

 ### بررسی پرداخت اخرین قست وام  
 if (testEndLoan(aghsat.loan)):
   loan = Loan.objects.get(id= aghsat.loan.id)
   print(loan) 
   loan.state = False
   loan.save()
 return HttpResponseRedirect('/modir/listdarkhast')
  

def taidePardakhtSandoghViwe(request , id):
 darkhastSanogh = DarkhastSandogh.objects.get(id = id)
 darkhastSanogh.acceptDate = datetime.date.today()
 zakhireh = darkhastSanogh.Zakhireh
 zakhireh.pardakht = datetime.date.today()
 zakhireh.save()
 darkhastSanogh.save()
  
  ###  افزایش موجودی صندوق 
 mojodi = MSandogh.objects.get()
 mojodi.mojodi += zakhireh.mablagh 
 mojodi.save()
  
 # افزایش مبلغ member 
 Cmember =  zakhireh.member 
 Cmember.mablagh += zakhireh.mablagh
 Cmember.save()
 return HttpResponseRedirect('/modir/listDarkhastPardakhtSandogh')


def listPardakhtToSandoghVieW(request , id):
  
  member = Member.objects.get(id=id)
  name = member.user.first_name + "  " +  member.user.last_name
  template_name = "list_pardakht_sandogh.html"

  # بررسی  و  ایجاد اقساط پرپاختی بهصندوق برای کاربر
  listdoreh = Doreh.objects.all()
  for l in listdoreh:
    if  (len(Zakhireh.objects.filter(doreh = l , member = member)) == 0):
      Zakhireh.objects.create(member = member,doreh=l, mablagh=l.configh.mablagh ,pardakht=None)

  list = Zakhireh.objects.filter(member = member, pardakht =  None )
     


  context = {
   'list'   :  list, 
   'name'  : name
   } 
     

  return render(request, template_name, context)


class mojodi(ListView):
  template_name = 'mojodi.html'
  model = MSandogh




