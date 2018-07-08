from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
    path('', views.HomeView.as_view(), name="index"),
    path('about/', views.ServiceAboutView.as_view(), name="about"),
    path('guide/', views.GuideLineView.as_view(), name="guide"),
    path('help/', views.HelpView.as_view(), name="help"),
    path('privacy/', views.PrivacyView.as_view(), name="privacy"),
    path('terms_of_service/', views.TermsOfServiceView.as_view(), name="terms_of_service"),
    path('users/', views.UsersView.as_view(), name="users"),
    path('inquiry/', views.InquiryView.as_view(), name="inquiry"),
    path('opinion/', views.OpinionView.as_view(), name="opinion"),
]
