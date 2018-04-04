from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('', views.EventListView.as_view(), name="event_list"),
]

