from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('skenar/', views.scenar, name='scenar'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('massage/', views.massage, name='massage'),
    path('reyki/', views.reyki, name='reyki'),
    path('laser/', views.laser, name='laser'),
]