from django.shortcuts import render
from django.http import Http404
from .models import Event

def events(request):
	try:
		latest = Event.objects.order_by('-pub_date')[:3] 
	except TemplateDoesNotExist:
		raise Http404('Упс! Возникла ошибка!')
	context = {'latest': latest}
	return render(request, 'events/event_page.html', context)
	
def event_by_id(request, event_id):
	try:
		list_of_events = Event.objects.all()
		current_event = Event.objects.get(pk=event_id)
	except TemplateDoesNotExist:
		raise Http404('Упс! Возникла ошибка!')	
	context = {'list_of_events': list_of_events, 'current_event': current_event}
	return render(request, 'events/event_in_detail.html', context)
