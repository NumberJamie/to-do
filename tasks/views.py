from abc import ABC

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import ListView, UpdateView, CreateView

from tasks.forms import TaskUpdateForm
from tasks.models import Tasks


def mark_completed(request, pk):
    obj = Tasks.objects.get(pk=pk)
    if obj.author == request.user:
        obj.complete = True
        obj.save()
        return redirect('task_list')


class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/task_list.html'
    paginate_by = 5
    model = Tasks
    extra_context = {'title': 'todo | tasks'}

    def get_queryset(self, *args, **kwargs):
        return Tasks.objects.all().filter(author=self.request.user, complete=False).order_by('-added_on')


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'tasks/task_update.html'
    model = Tasks
    extra_context = {'title': 'todo | tasks update'}
    form_class = TaskUpdateForm
    success_url = 'task_list'

    def test_func(self):
        this_task = self.get_object()
        if self.request.user == this_task.author:
            return True
        return False


class TaskCreateView(LoginRequiredMixin, CreateView, ABC):
    template_name = 'tasks/task_create.html'
    model = Tasks
    extra_context = {'title': 'todo | tasks create'}
    form_class = TaskUpdateForm
    success_url = 'task_list'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(TaskCreateView, self).form_valid(form)
