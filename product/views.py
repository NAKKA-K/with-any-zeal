from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

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
        messages.success(self.request, 'イベント: 「{}」を作成しました'.format(form.instance))
        return super().form_valid(form)


class EventUpdateView(UpdateView):
    """ Update of Event model """

    model = Event
    fields = ('name', 'description', 'readme')
    template_name = 'product/event_form.html'
    success_url = reverse_lazy('product:event_list')

    def form_valid(self, form):
        messages.success(self.request, 'イベント: 「{}」を更新しました'.format(form.instance))
        return super().form_valid(form)


class EventDetailView(DetailView):
    """ Detail of Event model """

    model = Event
    template_name = 'product/event_detail.html'
    context_object_name = 'event'
