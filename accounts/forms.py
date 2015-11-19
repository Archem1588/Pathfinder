from registration.forms import RegistrationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(RegistrationForm):
    is_happy = forms.ChoiceField(label="Are you feeling happy today?", choices=((True, 'Yes!'), (False, 'Not really')))

class EditProfileForm(RegistrationForm):
    username = forms.CharField(label='username')
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ['username', 'email']