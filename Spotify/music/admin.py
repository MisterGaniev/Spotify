from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *

# Register your models here.

@admin.register(Artist)
class Artist_admin(ModelAdmin):
    pass

@admin.register(Album)
class Album_admin(ModelAdmin):
    pass

@admin.register(Song)
class Song_admin(ModelAdmin):
    pass
