from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic import CreateView

from product.models import Event


# Create your views here.

class EventListView(ListView):
    """ List of Event model """

    model = Event
    template_name = 'product/event_list.hmtl'
    context_object_name = 'events'


class EventCreateView(CreateView):
    """ Create of Event model """

    model = Event
    fields = ('name', 'description', 'readme')
    template_name = 'product/event_form.html'
    success_url = reverse_lazy('product:event_list')

    def form_valid(self, form):
        form.instance.create_user = self.request.user
        return super().form_valid(form)
