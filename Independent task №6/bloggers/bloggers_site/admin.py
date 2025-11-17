from django.contrib import admin
from .models import Blogger
from .models import News
from .models import Content

@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'status', 'created']
    list_filter = ['status', 'category', 'created']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    date_hierarchy = 'created'
    ordering = ['status', 'name']
@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'status', 'publish']
    list_filter = ['status', 'publish']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['title', 'blogger', 'type', 'published_date']
    list_filter = ['type', 'published_date']
    search_fields = ['title', 'content_body']
    autocomplete_fields = ['blogger']