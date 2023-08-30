
from django.contrib import admin
from django.urls import path,include
from modir import views 

urlpatterns = [
    path('' , views.index ) ,
    path('admin/', admin.site.urls),
    path('modir/',include('modir.urls'))
    


]
