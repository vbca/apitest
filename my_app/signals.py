from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from my_app import models
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(pre_save, sender=models.Program)
def notification(sender, **kwargs):
    print(kwargs)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    print("cacho el signals")
    if created:
        Token.objects.create(user=instance)
    

