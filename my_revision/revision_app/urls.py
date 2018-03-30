from django.contrib import admin
from django.urls import path
from revision_app import views



app_name = 'revision_app'

urlpatterns = [
    path('user_login/', views.user_login, name='user_login'),
    path('register/', views.register, name='register'),
]
