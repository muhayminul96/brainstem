from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import OneToOneField
# Create your models here.

class Info(models.Model):
    username = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.username
