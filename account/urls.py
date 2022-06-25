from django.urls import path

from account import views

urlpatterns = [
    path('', views.account_render, name='account'),
]