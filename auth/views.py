import os
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from django.contrib.auth.forms import PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.views import PasswordChangeView as PasswordChangeBase
from django.contrib.auth.tokens import *
from django.core.mail import EmailMessage
from django.http import HttpResponse, HttpResponseForbidden

from config.settings.main import BASE_DIR
from accounts.views.LoginRequiredMessageMixin import LoginRequiredMessageMixin
from accounts.models import User


# Create your views here.

class PasswordChangeView(LoginRequiredMessageMixin, PasswordChangeBase):
    success_url = reverse_lazy('accounts:mypage')


EMAIL_RESET_TOKEN_TEXT = 'INTERNAL_RESET_TOKEN_URL'
INTERNAL_RESET_SESSION_TOKEN = '_password_reset_token'

# HACK: なぜかデフォルトのpassword_reset/が有効になっていて、このViewが使われていない
class PasswordResetView(FormView):
    form_class = PasswordResetForm
    template_name = 'registration/password_reset.html.haml'
    email_template_name = 'templates/registration/password_reset_email.txt'
    success_url = reverse_lazy('auth:password_reset_done')

    def form_valid(self, form):
        user = self.get_user_by_email(form.cleaned_data['email'])
        if user is None:
            return HttpResponseForbidden()

        token = default_token_generator.make_token(user)
        self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
        replace_url = self.request.build_absolute_uri(reverse('auth:password_reset_confirm', args = [token]))

        email_body = ""
        with open(os.path.join(BASE_DIR, self.email_template_name)) as email_template:
            email_body = email_template.read().replace(EMAIL_RESET_TOKEN_TEXT, replace_url)

        EmailMessage('【WaZ】パスワードの再設定について', email_body, to=[form.cleaned_data['email']]).send()
        return super().form_valid(form)

    def get_user_by_email(self, email):
        try:
            return User.objects.get(email = email)
        except User.DoesNotExist:
            return None

class PasswordResetDoneView(TemplateView):
    template_name = 'registration/password_reset_done.html.haml'

class PasswordResetConfirmView(FormView):
    form_class = SetPasswordForm
    template_name = 'registration/password_reset_confirm.html.haml'
    success_url = reverse_lazy('accounts:password_reset_complete')

# TODO: アクセス時点(dispatch?)で、URLのuidb64からuser.pkを求める
# TODO: userを取得し、token_generator.check_tokenでsessionのtokenとuserが一致するか確認する
# TODO: sessionを削除する

class PasswordResetCompleteView(TemplateView):
    template_name = 'registration/password_reset_complete.html.haml'


def pass_test(request):
    EmailMessage('passの再設定', 'passを再設定します', to=['scarlet6187aria@gmail.com']).send()
    return HttpResponse('ok! send mail.')
