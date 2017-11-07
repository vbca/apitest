from django.apps import AppConfig
from django.db.models.signals import post_save, pre_save

class MyAppConfig(AppConfig):
    name = 'my_app'
    label = "My application"
    
    def ready(self):
        from .signals import notification
        from . import models
        pre_save.connect(notification, sender=models.Program)