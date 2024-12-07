
from django.contrib import admin
from django.urls import path
from financeapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('service/', views.services, name='services'),
    path('starter/', views.starter, name='starter'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('team/', views.team, name='team'),
    path('resources/', views.resources, name='resources'),
    path('appointment/', views.appointment, name='appointment'),
    path('show/', views.show, name='show'),
]
