from django.urls import path

from users import views
from django.contrib.auth import views as auth_views

from users.forms import UserLoginForm

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterForm, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', authentication_form=UserLoginForm), name='login'),
]
