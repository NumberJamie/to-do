from django.shortcuts import render


def account_render(request):
    return render(request, 'account/account.html', {'title': 'todo | account'})
