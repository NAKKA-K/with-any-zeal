from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, CreateView, DeleteView
from django.http import Http404

from product.models import EventJoin, Event
from accounts.views import LoginRequiredMessageMixin

class EventJoinListView(ListView):
    """ Join list of Event """

    model = EventJoin
    template_name = 'product/event_join_list.html.haml'
    context_object_name = 'event_joins'

    def get_queryset(self):
        event_joins = EventJoin.objects.filter(
            event = Event.objects.get(pk = self.kwargs['pk'])
        )
        return event_joins

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk = self.kwargs['pk'])
        context['joined'] = [event_join.user
            for event_join in context['event_joins']
            if self.request.user.username == event_join.user.username]
        context['join_num'] = EventJoin.objects.filter(event = context['event']).count
        return context

        return context


class EventJoinView(LoginRequiredMessageMixin, CreateView):
    """ Join to the Event """

    model = EventJoin

    def get(self, request, **kwargs):
        event = Event.objects.get(pk = kwargs['pk'])
        event_join = EventJoin.objects.filter(
                         user = request.user,
                         event = event
                     )
        if event_join.count() > 0:
            messages.info(request, '既に参加しています')
            return redirect('product:event_join_list', pk = kwargs['pk'])

        try:
            EventJoin.objects.create(
                user = request.user,
                event = event
            )
            messages.success(request, 'イベントに参加しました')
        except:
            messages.error(request, 'イベントへ参加できませんでした')

        return redirect('product:event_join_list', pk = kwargs['pk'])


class EventWithdrawView(LoginRequiredMessageMixin, DeleteView):
    """ Withdraw from the event """

    def post(self, request, **kwargs):
        """ ignore the create_user and not join user """
        event = get_object_or_404(Event, pk = kwargs['pk'])
        #if event.create_user == request.user:
        #    messages.error(request, '主催者はイベントから離脱できません')
        #    return redirect('product:event_join_list', pk = kwargs['pk'])

        event_join = None
        try:
            event_join = get_object_or_404(EventJoin, event = event, user = request.user)
        except Http404:
            messages.error(request, 'イベントに参加していません')
            return redirect('product:event_join_list', pk = kwargs['pk'])

        event_join.delete()
        messages.success(request, 'イベントから離脱しました')
        return redirect('product:event_join_list', pk = kwargs['pk'])
