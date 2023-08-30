from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django_jalali.db import models as jmodels




# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mablagh = models.BigIntegerField()
    def __str__(self):
        return self.user.first_name + " " + self.user.last_name

      
class TypeLoan(models.Model):
    tybeName = models.CharField(max_length= 150)
    tedadAghsat = models.IntegerField()

    def __str__(self):
        return self.tybeName


class Loan(models.Model):
   objects = jmodels.jManager()
   tarikh = jmodels.jDateField()
   mablagh = models.BigIntegerField ()
   type = models.ForeignKey(TypeLoan , on_delete= models.CASCADE)
   member = models.ForeignKey(Member , on_delete=models.CASCADE)
   state = models.BooleanField(default=True) 

   def __str__(self):
        return self.type.tybeName + " for " + self.member.user.first_name + " " +  self.member.user.last_name

   def get_absolute_url(self):
    return reverse("listLoans", kwargs={"pk": self.pk})


class ConfighDoreh(models.Model):
    titel = models.CharField(max_length=4,null=True)
    mablagh = models.BigIntegerField()

    def __str__(self):
     return str(self.titel)

  
class Aghsat(models.Model):
    objects = jmodels.jManager()
    loan = models.ForeignKey(Loan , on_delete=models.CASCADE) 
    mablagh = models.BigIntegerField()
    tarikh = jmodels.jDateField(blank=False)   # due date
    pardakht  = jmodels.jDateField(blank=True,null=True)    # date of payment
    shomareh = models.IntegerField()

    def __str__(self):
        return "ghest shomare " + str(self.shomareh) + " for vame " + self.loan.member.user.first_name + self.loan.member.user.last_name


class Doreh(models.Model):
 configh = models.ForeignKey(ConfighDoreh , on_delete=models.CASCADE ,default=None,null=True)
 titel = models.CharField(max_length=6 , null=True)
 tarikh = jmodels.jDateField()
 def  __str__(self): 
  return str(self.titel)


class Zakhireh(models.Model):
   member = models.ForeignKey(Member , on_delete=models.CASCADE)
   doreh = models.ForeignKey(Doreh , on_delete=models.CASCADE)
   mablagh = models.BigIntegerField()
   pardakht = jmodels.jDateField(blank = True ,null = True)

   def __str__(self):
        return " pardakht to sandogh for  " + self.member.user.first_name + self.member.user.last_name


class Darkhast(models.Model): 
    objects = jmodels.jManager()
    discription = models.CharField(max_length=200)
    acceptDate = jmodels.jDateField(null=True, blank=True)
    deletDate =  jmodels.jDateField(null=True, blank=True)
    startDate =  jmodels.jDateField()
    Aghsat =   models.ForeignKey(Aghsat , on_delete=models.CASCADE )

    def __str__(self):
        num =  self.Aghsat.shomareh
        name = self.Aghsat.loan.member.user.first_name+ self.Aghsat.loan.member.user.last_name
        str  ="darkhast ghest shomareh {}  for vame {} ".format(num , name)
        return str 


class MSandogh(models.Model):
    mojodi = models.BigIntegerField() 

    def __str__(self):
        return str(self.mojodi)


class DarkhastSandogh(models.Model): 
    objects = jmodels.jManager()
    discription = models.CharField(max_length=200)
    acceptDate = jmodels.jDateField(null=True, blank=True)
    deletDate =  jmodels.jDateField(null=True, blank=True)
    startDate =  jmodels.jDateField()
    Zakhireh =   models.ForeignKey(Zakhireh , on_delete=models.CASCADE ,)

    def __str__(self):
        name = self.Zakhireh.member.user.first_name+ self.Zakhireh.member.user.last_name
        str  ="darkhast pardakht sandogh for {} ".format( name)
        return str 



   


