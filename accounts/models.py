from django.db import models
from registration.signals import user_registered
import django

django.setup()


class UserProfile(models.Model):
    user = models.CharField(max_length=200)
    email = models.EmailField(max_length=254)
    is_human = models.BooleanField()

    def __str__(self):
        return self.user

def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    profile.is_human = bool(request.POST["is_human"])
    profile.save()

user_registered.connect(user_registered_callback)
