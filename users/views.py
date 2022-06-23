from django.shortcuts import render

from tasks.models import Tasks


def task_count(reqeust):
    if reqeust.user:
        task_amount = Tasks.objects.filter(author=reqeust.user).count()
        if task_amount > 9:
            task_amount = '9+'
        return {'task_amount': task_amount}
