from celery import shared_task


@shared_task(name="notification")
def send_email():
    pass