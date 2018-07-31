from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import PasswordChangeView as PasswordChangeBase
from django.contrib.auth.views import PasswordResetView as PasswordResetBase
from django.contrib.auth.views import PasswordResetDoneView as PasswordResetDoneBase
from django.contrib.auth.views import PasswordResetConfirmView as PasswordResetConfirmBase
from django.contrib.auth.views import PasswordResetCompleteView as PasswordResetCompleteBase
from django.contrib.auth.tokens import *
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseForbidden

from config.settings.main import BASE_DIR
from accounts.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from accounts.models import User


# Create your views here.

class PasswordChangeView(LoginRequiredMessageMixin, PasswordChangeBase):
    success_url = reverse_lazy('accounts:mypage')


class PasswordResetView(PasswordResetBase):
    template_name = 'registration/password_reset.html.haml'
    email_template_name = 'registration/password_reset_email.txt'
    subject_template_name = 'registration/password_reset_subject.txt'
    success_url = reverse_lazy('auth:password_reset_done')


class PasswordResetDoneView(PasswordResetDoneBase):
    template_name = 'registration/password_reset_done.html.haml'


class PasswordResetConfirmView(PasswordResetConfirmBase):
    template_name = 'registration/password_reset_confirm.html.haml'
    success_url = reverse_lazy('auth:password_reset_complete')


class PasswordResetCompleteView(PasswordResetCompleteBase):
    template_name = 'registration/password_reset_complete.html.haml'

