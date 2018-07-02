from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView

from product.models import Event

# Create your views here.

class HomeView(ListView):
    """ home view. recent event viewer """

    model = Event
    template_name = 'home/index.html'
    context_object_name = 'events'
    queryset = Event.objects.all().order_by('-created_at')[:5]

    def get(self, request, **kwargs):
        return super().get(request, **kwargs)

class ServiceAboutView(TemplateView):
    """ """

    template_name = 'home/about.html'
