# coding: utf-8
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    documento = models.TextField()
    departamento = models.TextField()
    distrito = models.TextField()
    provincia = models.TextField()
    time_zone = models.TextField()