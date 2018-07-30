from django.urls import path

from auth import views

app_name = 'auth'

urlpatterns = [
    path('password_change/', views.PasswordChangeView.as_view(), name="pass_change"),

    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/set_password/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('pass_test/', views.pass_test, name="pass_test"),
]
