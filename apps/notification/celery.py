from celery import shared_task
from django.core.mail import EmailMultiAlternatives


@shared_task(name="notification")
def send_email(message: EmailMultiAlternatives):
    message.send()
