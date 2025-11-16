from django.contrib import admin
from .models import Joke, Picture

# Register your models here.

@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    list_display = ['text', 'contributor_name', 'created_at']
    search_fields = ['text', 'contributor_name']
    list_filter = ['created_at']


@admin.register(Picture)
class PictureAdmin(admin.ModelAdmin):
    list_display = ['image_url', 'contributor_name', 'created_at']
    search_fields = ['contributor_name']
    list_filter = ['created_at']
