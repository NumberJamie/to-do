from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from tasks.models import Tasks


class TaskListView(LoginRequiredMixin, ListView):
    template_name = 'tasks/task_list.html'
    paginate_by = 5
    model = Tasks
    extra_context = {'title': 'todo | tasks'}

    def get_queryset(self, *args, **kwargs):
        return Tasks.objects.all().filter(author=self.request.user).order_by('-added_on')
