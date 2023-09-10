from django.urls import path
from .views import *

app_name = 'product'

urlpatterns = [
    #logic
    
    path('', all_products, name='home'),
    path('store/', store, name='store'),
    path('<slug:slug>/', product_detail, name='product_detail'),
    path('store/search/', product_search, name='product_search'),
    path('add/sale/', make_sale, name='make_sale'),
    path('add/mail/', mails, name='mails'),
    # path('set/track/', track_product, name='track_product'),
    path('category/<slug:slug>/', category, name='category'),
    
    #CRM
    path('add/', add_product, name='add_product'),
    path('<int:pk>/edit/', edit_product, name='edit_product'),
    path('<int:pk>/delete/', delete_product, name='delete_product'),
    path('add_comment/<int:pk>/', add_comment, name='add_comment'),
    
]
