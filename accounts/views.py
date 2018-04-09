from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import ListView

from product import models as product
from accounts.models import User

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


class MypageView(TemplateView):
    template_name = 'accounts/mypage.html'


class ProfileView(ListView):
    model = product.Event
    context_object_name = 'create_events'
    template_name = 'accounts/profile.html'

    def get_queryset(self):
        user = None
        # is valid user
        try:
            user = User.objects.get(username = self.kwargs.get('user_name'))
        except User.DoesNotExist:
            print("query raise")
            raise Http404

        try:
            return product.Event.objects.filter(create_user = user)
        except product.Event.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = None
        # is valid user
        try:
            user = User.objects.get(username = self.kwargs.get('user_name'))
        except User.DoesNotExist:
            print("context raise")
            raise Http404
        context['user_name'] = user.username
        context['join_events'] = product.EventJoin.objects\
                                 .filter(user = user)
        return context
