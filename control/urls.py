from control import views
from django.urls import path

app_name = 'control'

urlpatterns = [
    path('main/', views.main, name='main'),  #127.0.0.1:8000/control/main/
    path('cart/', views.cart, name='cart'),  #127.0.0.1:8000/poll/cart/
    path('count/', views.count, name='count'),  #127.0.0.1:8000/poll/cart/
    path('register/', views.register, name='register'), #127.0.0.1:8000/control/register/
]
