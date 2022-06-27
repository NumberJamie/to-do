from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from tasks.models import Tasks
from users.forms import UserRegisterForm, ProfileRegisterForm


def task_count(request):
    if request.user.is_authenticated:
        task_amount = Tasks.objects.filter(author=request.user, complete=False).count()
        if task_amount > 9:
            task_amount = '9+'
        return {'task_amount': task_amount}
    return {'': ''}


def register(request):
    if request.POST == 'POST':
        form = UserRegisterForm(request.POST)
        form2 = ProfileRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            form2.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return redirect('task_list')
    else:
        form = UserRegisterForm()
        form2 = ProfileRegisterForm()
    context = {
        'form': form,
        'form2': form2
    }
    return render(request, 'users/register.html', context)
