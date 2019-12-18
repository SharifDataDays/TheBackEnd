
from django.contrib.auth.models import User
from django.db import models


from apps.translation.models import translatedTextField


class Post(models.Model):

    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField()
    post_title = translatedTextField(related_name='post_title')
    text = translatedTextField(related_name='text')
    post_description = translatedTextField(related_name='post_description')





class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    shown = models.BooleanField(default=True)
    reply_to = models.ForeignKey(
        'Comment', on_delete=models.CASCADE, null=True, blank=True)


class Tag(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='tags')
    name = translatedTextField(related_name='name')
    color = models.CharField(max_length=20)
