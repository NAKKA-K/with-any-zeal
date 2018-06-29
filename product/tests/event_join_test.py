from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from product.models import Event, EventJoin

# Create your tests here.
class EventUrlAccessTest(TestCase):
    def setUp(self):
        self.myuser = get_user_model().objects.create(username = 'testsan', password = 'password3')
        self.event = Event.objects.create(
            create_user = self.myuser,
            name = 'test',
            description = 'test desc',
            readme = 'test readme'
        )

    def test_get_event_joins(self):
        res = self.client.get(reverse('product:event_join_list'))
        self.assertTemplateUsed(res, 'product/event_list_join.html')
        self.assertEqual(res.status_code, 200)

    def test_non_logged_in_join_event(self):
        res = self.client.get(reverse('product:event_join', pk = 1))
        self.assertRedirects(response, reverse('login') + '?next=/product/event_join/')

    def test_logged_in_join_event(self):
        self.client.force_login(self.myuser)
        res = self.client.get(reverse('product:event_join', pk = 1))
        self.assertEqual(res.status_code, 200)

    def test_integration_join_event(self):
        res = self.client.get(reverse('product:event_join_list'))
        self.assertEqual(res.status_code, 200)

        # Event model count
        self.assertEqual(Event.objects.all().count(), 0)

        # non logged in event_join get
        res = self.client.get(reverse('product:event_join', pk = 1))
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Event.objects.all().count(), 0)

        # logged in event_join get
        self.client.force_login(self.myuser)
        res = self.client.get(reverse('product:event_join', pk = 1))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Event.objects.all().count(), 1)

    def test_integration_withdraw_event(self):
        EventJoin.objects.create(
            user = self.myuser,
            event = self.event)
        self.assertEqual(EventJoin.objects.all().count(), 1)

        # non logged in event_join get
        res = self.client.get(reverse('product:event_withdraw', pk = 1))
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Event.objects.all().count(), 1)

        # logged in event_join get
        self.client.force_login(self.myuser)
        res = self.client.get(reverse('product:event_join', pk = 1))
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Event.objects.all().count(), 0)
