from django.db import models
from django.contrib.auth.models import User


class Mento_Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Friend_Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title