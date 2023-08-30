"""
URL configuration for sandogh project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from modir import views

urlpatterns = [
    path('', views.listMember ),
    path('members/',views.listMember , name='listMember'),
    path('loan/<int:id>' , views.listLoans , name = "listLoans" ),
    path('loan/' , views.listallLoans , name = "listAllLoans" ),
    path('listaghsat/<int:id>' , views.listaghsat , name = "listaghsat" ),
    path('pardakhtloan/<int:id>' , views.pardakhtloan.as_view() , name = 'pardakhtLoan'),
    path('listdarkhast/', views.listDarkhastviwe.as_view()),
    path('createDarkhast/<int:id>' , views.creatDarkhastView, name = 'creadDarkhast'),
    path('createDarkhastSandogh/<int:id>' , views.creatDarkhastSandoghView, name = 'createDarkhastSandogh'),
    path('taidedarkhast/<int:id>' , views.taideDarkhastViwe , name = 'taideDarkhast'),
    path('taidePardakhtSandogh/<int:id>' , views.taidePardakhtSandoghViwe , name = 'taidePardakhtSandogh'),
    path('mojodisandogh' , views.mojodi.as_view(), name='mojodisandogh'),
    path('listpardakhtSandogh/<id>' , views.listPardakhtToSandoghVieW , name = 'listpardakhtSandogh' ),
    path('listDarkhastPardakhtSandogh/' , views.listDarkhastPardakhtSandoghViwe.as_view() , name = 'listDarkhastPardakhtSandogh' ),



    
]

