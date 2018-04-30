from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import User 


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    user_type = models.CharField(max_length=100)

class TaskDetails(models.Model):
    task_name = models.CharField(max_length=100)
    users = models.ManyToManyField(User)


