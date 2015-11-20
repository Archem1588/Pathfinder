from django.db import models
from registration.signals import user_registered
import django
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm

django.setup()

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    is_happy = models.BooleanField()

    def __str__(self):
        return self.user

def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user=user)
    form = UserRegistrationForm(request.POST)
    profile.email = form.profile["email"]
    profile.first_name = form.profile["first_name"]
    profile.last_name = form.profile["last_name"]
    profile.is_happy = bool(request.POST["is_happy"])
    profile.save()

user_registered.connect(user_registered_callback)
