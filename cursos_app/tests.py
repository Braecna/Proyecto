from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse


class LoginByEmailTests(TestCase):
    def test_login_accepts_email_when_username_is_different(self):
        user_model = get_user_model()
        user_model.objects.create_user(
            username='juan',
            email='juan@gmail.com',
            password='test-password-123',
        )

        response = self.client.post(reverse('login'), {
            'email': 'juan@gmail.com',
            'password': 'test-password-123',
        })

        self.assertRedirects(response, reverse('inicio'))
