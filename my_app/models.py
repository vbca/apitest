from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import validators
from django.contrib.auth.models import User


# Create your models here.
class Meetup(models.Model):
    name = models.CharField(max_length=50, help_text="Max length 50")
    logo = models.ImageField(null=True)

class Event(models.Model):
    name = models.CharField(max_length=200, help_text="Max length 200")
    date = models.DateField(auto_now=False, help_text="format dd-mm-yyyy", error_messages={"message":"Plese put a valid date"}, validators= [validators.validate_date_event])
    time = models.TimeField(auto_now=False)
    confirmed = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Program(models.Model):
    name = models.CharField(max_length=50)
    instructor = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"El programa es: {self.name}"

class PersonQuerySet(models.QuerySet):
    def younger(self):
        return self.filter(age__lte=25)

    def older(self):
        return self.filter(age__gte=30)

class PersonManager(models.Manager):
    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def younger(self):
        return self.get_queryset().younger()

    def older(self):
        return self.get_queryset().older()

class Person(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    program = models.ForeignKey(Program, related_name="program_person")
    age = models.IntegerField(default=0, help_text="solo numeros", validators=[validators.age_validation])

    objects = PersonManager()

    def __str__(self):
        return self.email

class EventPerson(models.Model):
    event = models.ForeignKey(Event, related_name="event_person")
    person = models.ForeignKey(Person, related_name="person_event")


from django.contrib.auth.models import User

################################################################
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user}"

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class Company(models.Model):
    name=models.CharField(max_length=50,help_text="Max length 50")
    validate = models.BooleanField(default=False)
    logo=models.ImageField(null=True)
    bussiness_type=models.CharField(max_length=20,help_text="Max length 20")
    city=models.CharField(max_length=30,help_text="Max length 30")
    domain=models.URLField(max_length=200,help_text="Max length 200")
    user=models.ForeignKey(User)

    def __str__(self):
        return self.name

class Complaint_Category(models.Model):
    name=models.CharField(max_length=50,help_text="Max length 50")

    def __str__(self):
        return self.name

class Complaint(models.Model):
    text_complaint=models.TextField()
    company = models.ForeignKey(Company, related_name='company')
    categories=models.ManyToManyField(Complaint_Category)
    created_time = models.DateTimeField('Created Time', auto_now_add=True,null=True)
    user = models.ForeignKey(User)

    def __str__(self):
        return (str(self.company))

#Django Mike
class Article(models.Model):
    title=models.TextField(max_length=254)
    body=models.TextField()
    likes=models.IntegerField()

class Comment(models.Model):
    article=models.ForeignKey(Article)
    text=models.TextField()

    
