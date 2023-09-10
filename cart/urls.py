from django.urls import path
from .views import *
app_name = 'cart'

urlpatterns = [
path('summary/', Cart_summary, name='cart_summary'),
path('add/', Cart_add, name='cart_add'),

path('update/', Cart_update, name='cart_update'),
path('delete/', Cart_delete, name='cart_delete'),

path('test/', test, name='cart_test'),

]