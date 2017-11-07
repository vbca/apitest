from django.contrib import admin
from . import models
from . import apps
# Register your models here.

'''admin.site.register(models.Person)
admin.site.register(models.Program)
admin.site.register(models.Event)
admin.site.register(models.Meetup)
admin.site.register(models.EventPerson)'''

admin.site.register(models.Profile)
admin.site.register(models.Company)
admin.site.register(models.Complaint_Category)
admin.site.register(models.Complaint)
admin.site.register(models.Article)
admin.site.register(models.Comment)