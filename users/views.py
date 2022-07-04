from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import ListView

from tasks.models import Tasks
from users.forms import UserCreateForm
from users.models import Profile


def task_count(request):
    if request.user.is_authenticated:
        task_amount = Tasks.objects.filter(author=request.user, complete=False).count()
        if task_amount > 9:
            task_amount = '9+'
        return {'task_amount': task_amount}
    return {'': ''}


def add_friend(request, pk):
    friend = User.objects.get(pk=pk)
    request.user.profile.following.add(friend)
    return redirect('user_list')


def block(request, pk):
    blocked = User.objects.get(pk=pk)
    request.user.profile.blocked.add(blocked)
    return redirect('user_list')


def register_render(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            auth_user = authenticate(username=username, password=password)
            login(request, auth_user)
            return redirect('task_list')
    else:
        form = UserCreateForm()
    context = {
        'form': form,
        'title': 'register',
    }
    return render(request, 'users/register.html', context)


class UserListView(LoginRequiredMixin, ListView):
    template_name = 'users/user_list.html'
    paginate_by = 5
    model = User
    extra_context = {'title': 'todo | users'}

    def get_queryset(self, *args, **kwargs):
        return User.objects.all().filter(is_active=True).exclude(following__user__in=User.objects.all()).order_by('-username')


def custom_page_not_found_view(request, exception):
    return render(request, "errorpages/404.html", {})


def custom_error_view(request, exception=None):
    return render(request, "errorpages/500.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "errorpages/403.html", {})


def custom_bad_request_view(request, exception=None):
    return render(request, "errorpages/400.html", {})
