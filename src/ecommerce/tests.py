import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model
from ecommerce import forms

User = get_user_model()


def create_user(username):
    """
    Create a question with the given `question_text` and published the
    given number of `days` offset to now (negative for questions published
    in the past, positive for questions that have yet to be published).
    """
    email = '{0}@email.com'.format(username)
    return User.objects.create_user(username, email, password=username)


class AuthViewTests(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'email': 'testuser@gmail.com',
            'password': 'secret'}


    def test_get_login_page(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_can_login(self):
        """
        If user exists, login.
        """
        User.objects.create_user(**self.credentials)
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_registration_view_get(self):
        """
        A ``GET`` to the ``register`` view uses the appropriate
        template and populates the registration form into the context.

        """
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'auth/register.html')
        self.failUnless(isinstance(
            response.context['form'], forms.RegisterForm))

    def test_registration_view_post_success(self):
        """
        A ``POST`` to the ``register`` view with valid data properly
        creates a new user and issues a redirect.

        """
        credentials = {
            'username': 'reg',
            'email': 'reg@gmail.com',
            'password': 'secret',
            'password2': 'secret'}
        response = self.client.post(reverse('register'), credentials)
        # self.assertRedirects(response,
        #                      'http://testserver%s' % reverse('login'))
        self.assertEqual(User.objects.count(), 1)

    def test_registration_view_post_failure(self):
        """
        A ``POST`` to the ``register`` view with invalid data does not
        create a user, and displays appropriate error messages.

        """
        credentials = {
            'username': 'reg',
            'email': 'reg@gmail.com',
            'password': 'secret',
            'password2': 'secretv'}
        response = self.client.post(reverse('register'), credentials)
        # self.assertEqual(response.status_code, 200)
        self.failIf(response.context['form'].is_valid())
        self.assertFormError(response, 'form', field=None,
                             errors="Passwords do not match")
