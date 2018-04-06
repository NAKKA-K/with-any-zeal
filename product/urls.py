from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('', views.EventListView.as_view(), name="event_list"),
    path('create/', views.EventCreateView.as_view(), name="event_create"),
    path('<int:pk>/update/', views.EventUpdateView.as_view(), name="event_update"),
    path('<int:pk>/detail/', views.EventDetailView.as_view(), name="event_detail"),
    path('<int:pk>/delete/', views.EventDeleteView.as_view(), name="event_delete"),
]

