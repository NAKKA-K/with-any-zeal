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


class EventJoin(models.Model):
    """ イベント参加テーブル """
    event = models.ForeignKey(Event, verbose_name = _('イベント'))
    user = models.ForeignKey(settins.AUTH_USER_MODEL, _('ユーザー'))


class EventSkillTag(models.Model):
    """ イベント技術タグテーブル """
    event = models.ForeignKey(Event, verbose_name = _('イベント'))
    tag = models.CharField(_('技術タグ'), max_length = 16)
