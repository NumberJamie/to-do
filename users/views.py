from django.shortcuts import render

from tasks.models import Tasks


def task_count(request):
    if request.user.is_authenticated:
        task_amount = Tasks.objects.filter(author=request.user, complete=False).count()
        if task_amount > 9:
            task_amount = '9+'
        return {'task_amount': task_amount}
    return {'': ''}
