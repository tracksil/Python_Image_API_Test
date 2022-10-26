from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Images)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('photo_id', 'title', 'album_id', 'dominant_color', 'width', 'height', 'url')
