from django.db import models
from django.contrib.auth.models import User


class Mento_Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    #좋아요 수
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

class Friend_Post(models.Model):
    author = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    post = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Mento_Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Mento_Post, null =True, blank=True, on_delete=models.CASCADE)
    writer = models.ForeignKey('users.User',on_delete=models.CASCADE)
    #댓글 작성자 학교,학과,학번
    #writer_profile = models.ForeignKey("Profile", null =True, blank=True, on_delete=models.CASCADE)
    
    # 좋아요 수
    like_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.comment

class Profile(models.Model):
    # user 학교,학과,학번
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)

    # 좋아요
    like_mentopost = models.ManyToManyField(Mento_Post, blank=True,related_name='like_users') 