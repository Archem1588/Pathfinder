from django.db import models
from registration.signals import user_registered
import django
from django.contrib.auth.models import User

django.setup()

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=254)
    is_happy = models.BooleanField()

    def __str__(self):
        return self.user


def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    profile.is_happy = bool(request.POST["is_happy"])
    profile.save()

user_registered.connect(user_registered_callback)
