from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Followers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")


class Post(models.Model):
    content = models.CharField(max_length=280)
    likes = models.ManyToManyField(User, related_name="liked_posts")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
