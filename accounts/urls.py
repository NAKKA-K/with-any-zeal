from django.urls import path
from django.views.generic.base import TemplateView

app_name = 'accounts'

urlpatterns = [
    path('', TemplateView.as_view(template_name='accounts/index.html'), name="index")
]
