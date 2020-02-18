from django.db import models

class Category(models.Model):
	name = models.CharField('Имя категории', blank=True, db_index=True, max_length = 200)
	slug = models.SlugField(null=True, max_length=40)
	description = models.TextField('Описание', null=True, blank=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'
		
class Detail(models.Model):
	category = models.ForeignKey(Category, null=True, on_delete = models.CASCADE)
	title = models.CharField('Название', max_length = 200)
	subtitle = models.CharField('Подзаголовок', null=True, max_length = 200)
	info = models.TextField('Информация', null=True, blank=True)	
	cover = models.ImageField(blank=True, upload_to='tours/', height_field=None, width_field=None, max_length=100)
	duration = models.CharField('Продолжительность', null=True, blank=True, max_length = 200)
	cost = models.CharField('Цена', null=True, max_length = 200)
	
	def __str__(self):
		return self.title	
		
	class Meta:
		verbose_name = 'Тур'
		verbose_name_plural = 'Туры'
		

