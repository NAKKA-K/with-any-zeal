from django.contrib import messages
from django.views.generic import CreateView

from product.models import EventJoin
from product.models import Event

class EventJoinView(CreateView):
    """ Join to the Event """

    model = EventJoin

    def get(self, request, **kwargs):
        try:
            EventJoin.objects.create(user = request.user,
                                     event = Event.objects.get(pk = kwargs['pk']))
            messages.error(request, 'イベントに参加しました')
        except:
            messages.error(request, 'イベントへ参加できませんでした')
        return None
