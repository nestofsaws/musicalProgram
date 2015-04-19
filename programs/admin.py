from django.contrib import admin
from . import models 

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    search_fields = ('title',)


class ArtistAdmin(admin.ModelAdmin):
    search_fields = ('last_name',)

 
class PerformerInline(admin.TabularInline):
    model = models.Performer
    extra = 2 # how many rows to show


class ProgramAdmin(admin.ModelAdmin):
 	search_fields = ('title',)
 	inlines = (PerformerInline,)


admin.site.register(models.Artist, ArtistAdmin)
admin.site.register(models.Song, SongAdmin)
admin.site.register(models.Program, ProgramAdmin)



