from django.urls import path
from .views import *
app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', create_user, name='create_user'),
    path('<int:pk>/edit/', edit_user, name='edit_user'),
    path('<int:pk>/delete/', delete_user, name='delete_user'),
    
]