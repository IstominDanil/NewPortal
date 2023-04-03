from django.db.models.signals import post_save, m2m_changed, pre_save
from django.dispatch import receiver
from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from .models import Post, Author, PostCategory
from django.utils import timezone
from datetime import datetime

@receiver(m2m_changed, sender=Post)
def mass_sender(sender, instance, action, **kwargs):
   if action == 'post_add':
       category = instance.post_category.all().values('subscribers')
       subscribers_list = []
       for i in category:
            for key in i:
               user = Author.objects.all().get(pk=i[key])
               subscribers_list.append(user.email)

       send_mail(
            subject=f'{instance.header}',
            message=f'{instance.text}',
            from_email='istomin.danil@mail.ru',
            recipient_list=subscribers_list
        )


@receiver(pre_save, sender = Author)
def check_for_saves(sender, instance, **kwargs):
    current_author = instance.author.id
    current_time = datetime.now(tz=timezone.utc)
    day = datetime(days=1)
    my_time = current_time - day

    for i in Post.objects.all().filter(author=current_author, published_date=my_time):
        if len(i) > 1:
            raise Exception("Sorry, you can't save more than 1 post per day.")
