from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DetailView
from django.views.generic import DeleteView

from product.models import Event, EventJoin
from accounts.views import LoginRequiredMessageMixin

# Create your views here.

class EventListView(ListView):
    """ List of Event model """

    model = Event
    template_name = 'product/event_list.html.haml'
    context_object_name = 'events'
    queryset = Event.objects.all().order_by('-created_at')


class EventCreateView(LoginRequiredMessageMixin, CreateView):
    """ Create of Event model """

    model = Event
    fields = ('name', 'description', 'readme')
    template_name = 'product/event_form.html.haml'
    success_url = reverse_lazy('product:event_list')

    def form_valid(self, form):
        form.instance.create_user = self.request.user
        form.save()
        form.instance.join_event() # Default join to create event
        messages.success(self.request, 'イベント: 「{}」を作成しました'.format(form.instance))
        return super().form_valid(form)


class EventUpdateView(LoginRequiredMessageMixin, UpdateView):
    """ Update of Event model """

    model = Event
    fields = ('name', 'description', 'readme')
    template_name = 'product/event_update.html.haml'
    success_url = reverse_lazy('product:event_list')

    def get(self, request, **kwargs):
        event = get_object_or_404(Event, pk = kwargs['pk'])
        if event.create_user != request.user:
            messages.info(self.request, 'イベント作成者以外は編集できません')
            return redirect('login')
        return super().get(request, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'イベント: 「{}」を更新しました'.format(form.instance))
        return super().form_valid(form)


class EventDetailView(DetailView):
    """ Detail of Event model """

    model = Event
    template_name = 'product/event_detail.html.haml'
    context_object_name = 'event'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['join_num'] = EventJoin.objects.filter(event = context['event']).count
        return context


class EventDeleteView(LoginRequiredMessageMixin, DeleteView):
    """ Delete of Event model """

    def get(self, request, **kwargs):
        event = get_object_or_404(Event, pk = kwargs['pk'])
        if event.create_user != request.user:
            messages.info(self.request, 'イベント作成者以外は編集できません')
            return redirect('login')
        event.delete()
        messages.success(self.request, 'イベント: 「{}」を削除しました'.format(event.name))
        return redirect('product:event_list')
