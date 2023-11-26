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
    user = models.ForeignKey(
        authModels.User,
        on_delete=models.RESTRICT
    )
    created_on = models.DateTimeField(auto_created=True)

class Activity(models.Model):
    KIND_CALL = "Call"
    KIND_EMAIL = "Email"
    KIND_TEXT = "Text"

    KIND_CHOICES = [
        (KIND_CALL, "Call"),
        (KIND_EMAIL, "Email"),
        (KIND_TEXT, "Text")
    ]

    contact = models.ForeignKey(
        Contact,
        on_delete=models.RESTRICT
        )
    created_on = models.DateTimeField(
        auto_now_add=True
    )
    kind = models.CharField(
        max_length=10,
        choices=KIND_CHOICES,
        default=KIND_CALL
        )
    
    text = models.TextField(
        blank=True,
        null=True
    )
    
    




