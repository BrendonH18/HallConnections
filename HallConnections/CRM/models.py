from django.db import models
from django.contrib.auth import models as authModels

class Contact(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    created_on = models.DateField(auto_now_add=True)

class Change(models.Model):
    user = models.ForeignKey(authModels.User, on_delete=models.RESTRICT)
    created_on = models.DateTimeField(auto_created=True)




