from django.contrib import messages
from django.shortcuts import redirect
from django.views.generic import ListView
from django.views.generic import CreateView

from product.models import EventJoin
from product.models import Event

class EventJoinListView(ListView):
    """ Join list of Event """

    model = EventJoin
    template_name = 'product/event_join_list.html'

    def get_queryset(self):
        return EventJoin.objects.filter(
            event = Event.objects.get(pk = self.kwargs['pk'])
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk = self.kwargs['pk'])
        return context


class EventJoinView(CreateView):
    """ Join to the Event """

    model = EventJoin

    def get(self, request, **kwargs):
        event_join = None
        try:
            event_join = EventJoin.objects.get(
                            user = request.user,
                            event = Event.objects.get(pk = kwargs['pk'])
                         )
        except:
            pass

        if event_join is not None:
            messages.info(request, '既に参加しています')
            return redirect('product:event_join_list', pk = kwargs['pk'])

        try:
            EventJoin.objects.create(user = request.user,
                                     event = Event.objects.get(pk = kwargs['pk']))
            messages.success(request, 'イベントに参加しました')
        except:
            messages.error(request, 'イベントへ参加できませんでした')
        return redirect('product:event_join_list', pk = kwargs['pk'])
