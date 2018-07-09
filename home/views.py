from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import ListView, TemplateView, CreateView

from accounts.views import LoginRequiredMessageMixin
from accounts.models import User
from product.models import Event
from home.models import Inquiry, Opinion

# Create your views here.

class HomeView(ListView):
    """ home view. recent event viewer """

    model = Event
    template_name = 'home/index.html'
    context_object_name = 'events'
    queryset = Event.objects.all().order_by('-created_at')[:5]

class ServiceAboutView(TemplateView):
    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event_num'] = Event.objects.count()
        context['user_num'] = User.objects.count()
        return context

class GuideLineView(TemplateView):
    template_name = 'home/guideline.html'

class HelpView(TemplateView):
    template_name = 'home/help.html.haml'

class PrivacyView(TemplateView):
    template_name = 'home/privacy.html.haml'

class TermsOfServiceView(TemplateView):
    template_name = 'home/terms_of_service.html'

class UsersView(ListView):
    model = User
    context_object_name = 'users'
    queryset = User.objects.all().order_by('-created_at')
    template_name = 'home/users.html'

class InquiryView(LoginRequiredMessageMixin, CreateView):
    model = Inquiry
    fields = ('title', 'body')
    template_name = 'home/inquiry.html'
    success_url = reverse_lazy('product:event_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'ご質問には確認でき次第、対応させていただきます')
        return super().form_valid(form)

class OpinionView(LoginRequiredMessageMixin, CreateView):
    model = Opinion
    fields = ('body',)
    template_name = 'home/opinion.html'
    success_url = reverse_lazy('product:event_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'ご意見ありがとうございます')
        return super().form_valid(form)
