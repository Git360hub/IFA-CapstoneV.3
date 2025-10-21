from django.urls import path
from . import views

urlpatterns = [
 path('', views.home_view, name='home'),
 path('about/', views.about_view, name='about'),
 path('contact/', views.contact_view, name='contact'),
 path('plants/', views.plants_view, name='plants'),
 path('home/', views.home_view, name='home'),
 path('faq/', views.faq_view, name='faq'),
 path('membersonly/', views.membersonly_view, name='membersonly'),
]