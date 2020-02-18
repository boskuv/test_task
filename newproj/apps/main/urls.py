from django.urls import path
from django.views.generic import TemplateView
from .views import main

app_name = 'main'
urlpatterns = [
	path('', main, name = 'main'),
	path('about/', TemplateView.as_view(template_name="main/about.html"))
]
