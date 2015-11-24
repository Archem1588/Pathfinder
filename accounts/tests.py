import datetime
import _sha256

from django.conf import settings
from django.contrib.auth.models import User
from django.core import mail
from django.core import management
from django.core.urlresolvers import reverse
from django.test import TestCase

from registration import forms
# from accounts import forms
from registration.models import RegistrationProfile


class RegistrationTestCase(TestCase):
    """
    Base class for the test cases; this sets up two users -- one
    expired, one not -- which are used to exercise various parts of
    the application.
    
    """
    def setUp(self):
        self.sample_user = RegistrationProfile.objects.create_inactive_user(username='alice',
                                                                            password='secret',
                                                                            email='alice@example.com')
        self.expired_user = RegistrationProfile.objects.create_inactive_user(username='bob',
                                                                             password='swordfish',
                                                                             email='bob@example.com')
        self.expired_user.date_joined -= datetime.timedelta(days=settings.ACCOUNT_ACTIVATION_DAYS + 1)
        self.expired_user.save()


class RegistrationModelTests(RegistrationTestCase):
    """
    Tests for the model-oriented functionality of django-registration,
    including ``RegistrationProfile`` and its custom manager.
    
    """
    def test_new_user_is_inactive(self):
        """
        Test that a newly-created user is inactive.
        
        """
        self.failIf(self.sample_user.is_active)

    def test_registration_profile_created(self):
        """
        Test that a ``RegistrationProfile`` is created for a new user.
        
        """
        self.assertEqual(RegistrationProfile.objects.count(), 2)

    def test_activation_email(self):
        """
        Test that user signup sends an activation email.
        
        """
        self.assertEqual(len(mail.outbox), 2)

    def test_account_expiration_condition(self):
        """
        Test that ``RegistrationProfile.activation_key_expired()``
        returns ``True`` for expired users and for active users, and
        ``False`` otherwise.
        
        """
        # Unexpired user returns False.
        self.failIf(RegistrationProfile.objects.get(user=self.sample_user).activation_key_expired())

        # Expired user returns True.
        self.failUnless(RegistrationProfile.objects.get(user=self.expired_user).activation_key_expired())

        # Activated user returns True.
        RegistrationProfile.objects.activate_user(RegistrationProfile.objects.get(user=self.sample_user).activation_key)
        self.failUnless(RegistrationProfile.objects.get(user=self.sample_user).activation_key_expired())


class RegistrationFormTests(RegistrationTestCase):
    """
    Tests for the forms and custom validation logic included in
    django-registration.
    
    """
    def test_registration_form(self):
        """
        Test that ``RegistrationForm`` enforces matching passwords.
        
        """
        invalid_data_dicts = [
            # Non-alphanumeric username.
            {
            'data':
            { 'username': 'foo',
              'email': 'foo@example.com',
              'password1': 'foo',
              'password2': 'bar',
              'first_name': 'foo',
              'last_name': 'bar'},
            'error':
            ('__all__', [u"You must type the same password each time"])
            },
            ]

        for invalid_dict in invalid_data_dicts:
            form = forms.RegistrationForm(data=invalid_dict['data'])
            self.failIf(form.is_valid())
