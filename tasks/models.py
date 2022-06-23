from django.contrib.auth.models import User
from django.db import models


class Tasks(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255)
    task_description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()

    def __str__(self):
        return f'{self.author} | {self.task_name}'


class TaskCategory(models.Model):
    class Meta:
        unique_together = ['author', 'category_name']

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category_name = models.CharField(max_length=255)
    category_description = models.TextField()
    tasks = models.ManyToManyField(Tasks)
    added_on = models.DateTimeField(auto_now_add=True)
    due = models.DateTimeField()

    def __str__(self):
        return f'{self.author} | {self.category_name}'
