from django.contrib import admin
from programs.models import Song, Artist, Program

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    search_fields = ('title',)

admin.site.register(Song, SongAdmin)

class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('last_name',)

admin.site.register(Artist, ArtistAdmin)
 
class ProgramAdmin(admin.ModelAdmin):
 	search_fields = ('title',)

admin.site.register(Program, ProgramAdmin)