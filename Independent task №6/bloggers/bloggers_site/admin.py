from django.contrib import admin
from .models import Blogger

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'status', 'created']
    list_filter = ['status', 'category', 'created']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
    ordering = ['status', 'name']
