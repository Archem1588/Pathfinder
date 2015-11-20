from registration.forms import RegistrationForm
from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(RegistrationForm):
    is_happy = forms.ChoiceField(label="Are you feeling happy today?", choices=((True, 'Yes!'), (False, 'Not really')))

class EditProfileForm(RegistrationForm):
    username = forms.CharField(label='username')
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='email')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']