
from django.urls import path

from schoolapp import views

app_name = 'schoolapp'

urlpatterns = [
    path('', views.base, name='base'),
    path('button/', views.button, name='button'),
    path('form/', views.form, name='form'),
    path('order/', views.confirmed_order, name='order')
    ]
