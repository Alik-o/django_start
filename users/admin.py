from click import group
from django.contrib import admin
from .models import User


@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('email', 'username', 'phone', 'country')
    list_filter = ('email', 'username', 'phone', 'country',)
    search_fields = ('email',)
