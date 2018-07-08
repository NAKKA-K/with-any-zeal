from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings

# Create your models here.

class Inquiry(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name = _('ご質問作成ユーザー'),
        on_delete = models.PROTECT
    )
    title = models.CharField(_('質問タイトル'), max_length = 128)
    body = models.TextField(_('本文'))
    created_at = models.DateTimeField(_('質問作成日'), auto_now_add = True)

class Opinion(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name = _('ご意見作成ユーザー'),
        on_delete = models.PROTECT
    )
    body = models.TextField(_('本文'))
    created_at = models.DateTimeField(_('質問作成日'), auto_now_add = True)

