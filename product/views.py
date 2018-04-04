from django.shortcuts import render
from django.views.generic import ListView

from product.views import Event


# Create your views here.

class EventListView(ListView):
    """ List of Event view """

    model = Event
    template_name = 'event_list.hmtl'


