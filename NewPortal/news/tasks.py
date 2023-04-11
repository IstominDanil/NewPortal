from celery import shared_task
from .models import *
import time
from django.core.mail import send_mail

@shared_task
def action():

    send_mail(
        subject=f'{Post.header}',
        message=f'{Post.text}',
        from_email='istomin.danil@mail.ru',
        recipient_list='subscribers_list'
    )

