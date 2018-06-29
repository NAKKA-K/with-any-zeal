from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from product.models import Event

# Create your tests here.
class EventUrlAccessTest(TestCase):
    def setUp(self):
        self.myuser = get_user_model().objects.create(username = 'testsan', password = 'password3')
        Event.objects.create(
            create_user = self.myuser,
            name = 'test',
            description = 'test desc',
            readme = 'test readme'
        )

    def test_non_logged_in_event_list_access(self):
        response = self.client.get(reverse('product:event_list'))
        self.assertTemplateUsed(response, 'product/event_list.html')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_event_list_access(self):
        self.client.force_login(self.myuser)
        response = self.client.get(reverse('product:event_list'))
        self.assertTemplateUsed(response, 'product/event_list.html')
        self.assertEqual(response.status_code, 200)

    def test_logged_in_event_create_post(self):
        self.assertEqual(Event.objects.all().count(), 1)
        self.client.force_login(self.myuser)
        response = self.client.post(reverse('product:event_create'), {
            'name': 'test event',
            'description': 'test',
            'readme': 'testtest'
        }, follow=True)
        self.assertEqual(response.status_code, 200) # success create if redirect to list
        self.assertRedirects(response, reverse('product:event_list') + '')
        self.assertTemplateUsed(response, 'product/event_list.html')
        self.assertEqual(Event.objects.all().count(), 2)

    def test_non_logged_in_event_create_post(self):
        response = self.client.post(reverse('product:event_create'), {
            'name': 'test event',
            'description': 'test',
            'readme': 'testtest'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?next=/product/create/')

    def test_logged_in_event_update_post(self):
        self.client.force_login(self.myuser)
        response = self.client.post(reverse('product:event_update', kwargs = {'pk': 1}), {
            'description': 'test',
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/event_form.html')

    def test_non_logged_in_event_update_post(self):
        response = self.client.post(reverse('product:event_update', kwargs = {'pk': 1}), {
            'description': 'test',
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login') + '?next=/product/1/update/')

    def test_logged_in_event_delete_access(self):
        self.assertEqual(Event.objects.all().count(), 1)
        self.client.force_login(self.myuser)
        response = self.client.get(reverse('product:event_delete', kwargs = {'pk': 1}))
        self.assertEqual(response.status_code, 302) # success create if redirect to list
        self.assertRedirects(response, reverse('product:event_list'))
        self.assertEqual(Event.objects.all().count(), 0)

    def test_non_logged_in_event_delete_access(self):
        response = self.client.get(reverse('product:event_delete', kwargs = {'pk': 1}))
        self.assertEqual(response.status_code, 302) # not success access if redirect to login
        self.assertRedirects(response, reverse('login') + '?next=/product/1/delete/')
        self.assertEqual(Event.objects.all().count(), 1)
