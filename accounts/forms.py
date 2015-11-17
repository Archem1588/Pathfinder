from registration.forms import RegistrationForm
from django import forms

class UserRegistrationForm(RegistrationForm):
    is_human = forms.ChoiceField(label="Are you human?:", choices=((True, 'True'), (False, 'False')))
