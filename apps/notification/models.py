import markdown
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

from django.db import models
from apps.notification.celery import *


# Create your models here.


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    text = models.TextField(max_length=200, null=False)
    seen = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.text


class Subscriber(models.Model):
    email = models.EmailField(null=False, unique=True)

    def __str__(self):
        return self.email


class EmailText(models.Model):
    subject = models.CharField(null=False, max_length=100)
    text = models.TextField(null=False)
    html = models.TextField(editable=False)

    def __str__(self):
        return self.text

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.html = markdown.markdown(self.text)
        subscribers = Subscriber.objects.all().values()

        for i in range(0, subscribers.count() + 1, 20):
            send_email.apply_async(
                kwargs={'subject': self.subject, 'text': self.text, 'to': list(subscribers[i:i + 20])})
