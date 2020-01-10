import string

from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task(name="notification")
def send_email(subject: string, text: string, to: list):
    context = {
        'subject': subject,
        'context': text
    }
    email_html_message = render_to_string('email/notification.html', context)
    email_plaintext_message = render_to_string('email/notification.txt', context)
    msg = EmailMultiAlternatives(subject=subject, from_email="datadays.sharif@gmail.com",
                                 cc=to, body=email_plaintext_message)
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()
