from django.shortcuts import render, redirect
from django.views.generic import ListView

from product.models import Event

# Create your views here.

class HomeView(ListView):
    """ home view. recent event viewer """

    model = Event
    template_name = 'home/index.html'
    context_object_name = 'events'
    queryset = Event.objects.all()[:5]

    def get(self, request, **kwargs):
        if request.user.is_authenticated:
            return redirect('product:event_list')
        return super().get(request, **kwargs)
