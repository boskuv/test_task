from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Category, Detail

class DetailAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'  # ('info',)
	
admin.site.register(Category)
admin.site.register(Detail, DetailAdmin)