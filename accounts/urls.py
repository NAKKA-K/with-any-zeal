from django.urls import path
from django.views.generic.base import TemplateView

from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name="signup"),
    path('mypage/', views.MypageView.as_view(), name="mypage"),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name="user_update"),
    path('<slug:user_name>/', views.ProfileView.as_view(), name="profile"),
]
