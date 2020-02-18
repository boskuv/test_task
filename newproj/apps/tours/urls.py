from django.urls import path

from .views import main, fiter_categ, find_tour

app_name = 'tours'
urlpatterns = [
	path('', main, name = 'main'),
	path('<slug:category_slug>/', fiter_categ, name = 'fiter_categ'),
	path('<slug:category_slug>/<int:tour_id>/', find_tour, name = 'find_tour'),
]
