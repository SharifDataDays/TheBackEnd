import markdown
from django.contrib.auth.models import User
from django.template.loader import render_to_string

from apps.notification.celery import *
from django.db import models

# Create your models here.
from rest_framework.validators import UniqueValidator


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
        subscribers = Subscriber.objects.all()

        context = {
            'subject': self.subject,
            'context': self.text
        }
        email_html_message = render_to_string('email/notification.html', context)
        email_plaintext_message = render_to_string('email/notification.txt', context)
        for index in range(start=0, stop=subscribers.count() + 1, step=20):
            message = EmailMultiAlternatives(subject=self.subject, from_email="datadays.sharif@gmail.com",
                                             cc=subscribers, body=email_plaintext_message)
            message.attach_alternative(email_html_message, "text/html")
            send_email.apply_async(message)
