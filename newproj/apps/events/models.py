from django.db import models

class Event(models.Model):
	title = models.CharField('Заголовок', db_index=True, max_length = 200)
	subtitle = models.TextField('Подзаголовок',null=True, blank=True)
	cover = models.ImageField(blank=True, upload_to='events/', height_field=None, width_field=None, max_length=100)
	pub_date = models.DateTimeField('Дата публикации', auto_now_add=True, db_index=True)

	def __str__(self):
		return self.title
	
	class Meta:
		verbose_name = 'Мероприятие'
		verbose_name_plural = 'Мероприятия'
