from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('kayit', views.EmailKayit, name='kayit'),
    path('liste',views.EmailListe,name='liste')
]