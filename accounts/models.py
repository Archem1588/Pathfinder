from django.db import models
import django
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm

django.setup()

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_happy = models.BooleanField()

    def __str__(self):
        return self.user
