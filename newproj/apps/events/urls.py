from django.urls import path

from .views import events, event_by_id 

app_name = 'events'
urlpatterns = [
	path('', events, name = 'events'),	
	path('<int:event_id>/', event_by_id, name = 'event_by_id'),
]
