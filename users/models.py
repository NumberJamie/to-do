from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture', default='profile_picture/default.png')
    following = models.ManyToManyField(User, related_name='following', blank=True)
    blocked = models.ManyToManyField(User, related_name='blocked', blank=True)

    def __str__(self):
        return f'{self.user}'
