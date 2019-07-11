from django.core.signals import request_finished, request_started
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from App.tasks import *

from App.models import Task


# to connect signal you need import it in apps.py

@receiver(post_save, sender=Task)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("task signal called")
        process.delay()

#
# @receiver(post_save, sender=Task)
# def save_user_profile(sender, instance, **kwargs):
#     print("task signal 2 called")
