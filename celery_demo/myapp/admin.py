from django.contrib import admin

from myapp.models import Blog
# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption']
    list_display_links = ['caption']
