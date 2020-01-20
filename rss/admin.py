from django.contrib import admin
from .models import RSS
# Register your models here.

@admin.register(RSS)
class RssAdmin(admin.ModelAdmin):
    fields = ('link', 'user')

