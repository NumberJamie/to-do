from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from users.models import Profile


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        self.fields['username'].help_text = 'Your username'
        self.fields['password'].help_text = 'Password so we know it is you'

    error_css_class = 'input-error'


class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']

    error_css_class = 'input-error'
