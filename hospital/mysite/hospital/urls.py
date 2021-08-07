from django.urls import path
from . import views






urlpatterns = [
    path('', views.page1, name='page1'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('doctor/', views.doctor, name='doctor')
]