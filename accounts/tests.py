from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.
class AccounUrlAccessTest(TestCase):
    def setUp(self):
        self.myuser = get_user_model().objects.create(username = 'testsan', password = 'password3')

    def test_signup_get_request(self):
        response = self.client.get(reverse('accounts:signup'))
        self.assertEqual(response.status_code, 200)

    def test_signup_post_request(self):
        response = self.client.post(reverse('accounts:signup'), {
            'username':'test_user',
            'password1':'test1234',
            'password2':'test1234',
        })
        self.assertEqual(response.status_code, 302) # Redirect to login if success
        self.assertEqual(get_user_model().objects.all().count(), 2)

    def test_not_logged_in_mypage_access(self):
        response = self.client.get(reverse('accounts:mypage'))
        self.assertEqual(response.status_code, 302)

    def test_logged_in_mypage_access(self):
        self.client.force_login(self.myuser)
        response = self.client.get(reverse('accounts:mypage'))
        self.assertEqual(response.status_code, 200)

    def test_exists_user_profile_access(self):
        response = self.client.get(reverse('accounts:profile', kwargs = {'user_name': self.myuser.username}))
        self.assertEqual(response.status_code, 200)

    def test_not_exists_user_profile_access(self):
        response = self.client.get(reverse('accounts:profile', kwargs = {'user_name': 'not_exists'}))
        self.assertEqual(response.status_code, 404)