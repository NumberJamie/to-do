from django.urls import path

from users import views

urlpatterns = [
    path('', views.base_render, name='base'),
]
