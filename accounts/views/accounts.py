from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404
from django.views.generic import CreateView, UpdateView, TemplateView, ListView

from product.models import Event, EventJoin
from accounts.models import User
from accounts.forms import UserCreationForm
from accounts.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html.haml'


class MypageView(LoginRequiredMessageMixin, TemplateView):
    template_name = 'accounts/mypage.html.haml'

class UserUpdateView(LoginRequiredMessageMixin, UpdateView):
    model = User
    fields = ('email',)
    template_name = 'accounts/user_update.html.haml'
    success_url = reverse_lazy('accounts:mypage')

class ProfileView(ListView):
    model = Event
    context_object_name = 'create_events'
    template_name = 'accounts/profile.html.haml'

    def get_queryset(self):
        # is valid user
        user = get_object_or_404(User, username = self.kwargs.get('user_name'))

        try:
            return Event.objects.filter(create_user = user)
        except Event.DoesNotExist:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # is valid user
        user = get_object_or_404(User, username = self.kwargs.get('user_name'))
        context['user'] = user
        context['join_events'] = EventJoin.objects.filter(user = user)
        return context

