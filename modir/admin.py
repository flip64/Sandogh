from django.contrib import admin
from modir.models import Member,Loan,Aghsat,TypeLoan,Darkhast,MSandogh,Doreh,Zakhireh,DarkhastSandogh
from modir.models import ConfighDoreh
# Register your models here.
admin.site.register(Member)
admin.site.register(Loan)
admin.site.register(TypeLoan)
admin.site.register(Aghsat)
admin.site.register(Darkhast)
admin.site.register(MSandogh)
admin.site.register(Doreh)
admin.site.register(Zakhireh)
admin.site.register(DarkhastSandogh)
admin.site.register(ConfighDoreh)


