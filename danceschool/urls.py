from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('', main, name='home'),
    path('login/', user_login, name='login'),
    path('sign-up/', sign_up, name = 'sign up'),
    path('logout/', user_logout, name='logout'),
    # path('edit/', edit, name = 'edit'),
    # path('profile/<int:pk>/edit/',UpdateView.as_view(), name='edit'),
    path('profile/', profile, name='edit'),
    path('password/', ChangePasswordView.as_view(), name='password'),
]