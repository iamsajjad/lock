from django.conf import settings
from django.urls import path, include
# import views from application
from .views import *

urlpatterns = [
    path('', accountsPage, name='accountsPage'),
    path('login/', loginPage, name='loginPage'),
    path('home/', homepage, name='home'),
    path('signIn/', signIn, name='signIn'),
    path('signUp/', signUp, name='signUp'),
    path('signOut/', signOut, name='signOut'),
]
