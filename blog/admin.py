from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'count_views', 'publication_attribute', 'content')
    list_filter = ('created_at',)
    search_fields = ('title', 'content')
