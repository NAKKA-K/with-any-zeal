from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class AccounUrlAccessTest(TestCase):
    def setUp(self):
        pass

    def test_signup_access(self):
        client = self.client
        response = client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

        response = client.post(reverse('accounts:signup'), {
            'username':'test_user',
            'password1':'test1234',
            'password2':'test1234',
        })
        self.assertEqual(response.status_code, 302) # Redirect to login if success
        self.assertEqual(get_user_model().objects.all().count(), 1)

    def test_mypage_access(self):
        pass

    def test_profile_access(self):
        pass
