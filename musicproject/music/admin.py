from django.contrib import admin

# Register your models here.

from .models import Album, Song

class SongInline(admin.TabularInline):
    model = Song

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SongInline]

admin.site.register(Album, AlbumAdmin)
