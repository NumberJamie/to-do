from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from tasks.models import Tasks
from users.forms import UserRegisterForm


def task_count(request):
    if request.user.is_authenticated:
        task_amount = Tasks.objects.filter(author=request.user, complete=False).count()
        if task_amount > 9:
            task_amount = '9+'
        return {'task_amount': task_amount}
    return {'': ''}


def register(request):
    if request.POST == 'POST':
        form = UserRegisterForm()
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if username is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html', context)
