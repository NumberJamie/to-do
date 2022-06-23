from django.shortcuts import render


def base_render(reqeust):
    return render(reqeust, 'base.html', {'title': 'todo | base'})
