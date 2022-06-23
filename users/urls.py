from django.urls import path

from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
