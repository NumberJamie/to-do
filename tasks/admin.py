from django.contrib import admin

from tasks.models import Tasks, TaskCategory

admin.site.register(Tasks)
admin.site.register(TaskCategory)
