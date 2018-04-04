from django.contrib import admin

from product.models import Event
from product.models import EventJoin
from product.models import EventSkillTag

# Register your models here.
admin.site.register(Event)
admin.site.register(EventJoin)
admin.site.register(EventSkillTag)

