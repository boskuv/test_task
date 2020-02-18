from django.shortcuts import render
from django.http import Http404
from .models import Category, Detail

def main(request): 
	try:
		list_of_categories = Category.objects.all()
	except TemplateDoesNotExist:
		raise Http404('Упс! Возникла ошибка!')	
	context = {'list_of_categories': list_of_categories}
	return render(request, 'tours/list_of_tours.html', context)
	
def fiter_categ(request, category_slug):
	try:
		list_of_tours = Detail.objects.filter(category__slug=category_slug)
		list_of_categories = Category.objects.all()
		meta_categ = Category.objects.get(slug=category_slug)
	except TemplateDoesNotExist:
		raise Http404('Упс! Возникла ошибка!')	
	context = { 'list_of_tours': list_of_tours, 'meta_categ': meta_categ, 'list_of_categories': list_of_categories}
	return render(request, 'tours/tours_by_categories.html', context)
	
def find_tour(request, category_slug, tour_id):
	try:
		current_tour = Detail.objects.get(pk=tour_id)
	except TemplateDoesNotExist:
		raise Http404('Упс! Возникла ошибка!')	
	context = { 'current_tour': current_tour}
	return render(request, 'tours/tour_in_detail.html', context)
