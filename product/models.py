from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.conf import settings


# Create your models here.
class Event(models.Model):
    """ イベントテーブル """
    create_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name = _('イベント作成ユーザ'),
        on_delete = models.PROTECT
    )
    name = models.CharField(_('イベント名'), max_length = 64)
    description = models.TextField(_('イベント概略'))
    readme = models.TextField(_('説明'))
    published_date = models.DateTimeField(_('公開日'), null = True)
    created_at = models.DateTimeField(_('作成日'), auto_now_add = True)

    def __str__(self):
        return self.name

    def join_event(self):
        EventJoin.objects.create(
            event = self,
            user = self.create_user)

class EventJoin(models.Model):
    """ イベント参加テーブル """
    event = models.ForeignKey(
        Event,
        verbose_name = _('イベント'),
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name = _('ユーザー'),
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.user.username


class EventSkillTag(models.Model):
    """ イベント技術タグテーブル """
    event = models.ForeignKey(
        Event,
        verbose_name = _('イベント'),
        on_delete = models.CASCADE
    )
    tag = models.CharField(_('技術タグ'), max_length = 16)

    def __str__(self):
        return self.tag

