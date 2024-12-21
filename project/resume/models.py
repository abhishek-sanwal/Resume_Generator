from django.db import models

# Create your models here.


class Profile(models.Model):
    name: str = models.CharField(max_length=200)
    email: str = models.CharField(max_length=200)
    phone: str = models.CharField(max_length=200)
    summary: str = models.TextField(max_length=2000)
    degree: str = models.CharField(max_length=200)
    school: str = models.CharField(max_length=200)
    university: str = models.CharField(max_length=200)
    previous_work: str = models.TextField(max_length=1000)
    skills: str = models.TextField(max_length=1000)
