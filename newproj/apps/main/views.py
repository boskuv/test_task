from django.shortcuts import render
from django.http import Http404
from events.models import Event
from tours.models import Category

def main(request):
	try:
		latest = Event.objects.order_by('-pub_date')[:3] 
		group_by_tours = Category.objects.all()
	except TemplateDoesNotExist:
		raise Http404('Упс! Возникла ошибка!')
	context = {'latest': latest, 'group_by_tours' : group_by_tours}
	return render(request, 'main/main_page.html', context)