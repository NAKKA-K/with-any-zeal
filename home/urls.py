from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('about/', views.ServiceAboutView.as_view(), name="about"),
]
