from asyncio.base_subprocess import WriteSubprocessPipeProto
from operator import truediv
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

class User(AbstractUser):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('C', 'Custum'),
    ]
    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    user_name = CharField(blank=True, max_length=255)
    profile_photo = models.ImageField(blank=True)
    website = models.URLField(blank=True)
    bio = models.TextField(blank=True)
    email = CharField(blank=True, max_length=255)
    phone_number = CharField(blank=True, max_length=255)
    gender =  CharField(blank=True, choices=GENDER_CHOICES, max_length=255)
    followers = models.ManyToManyField("self")
    folloing = models.ManyToManyField("self")
    

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
