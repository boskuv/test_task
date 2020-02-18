from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Event

class EventAdmin(SummernoteModelAdmin):  
    summernote_fields = '__all__'  # ('info',)

admin.site.register(Event, EventAdmin)