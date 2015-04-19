from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)    
    url = models.URLField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='artist/photo/')

    class Meta(object):
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return '%s, %s' %(self.last_name, self.first_name) 


class Song(models.Model):
    title = models.CharField(max_length=50)
    key = models.CharField(max_length=10, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    composed_on = models.IntegerField(max_length=4, null=True, blank=True)
    composer = models.CharField(max_length=50, null=True, blank=True)
  
    class Meta(object):
        ordering = ('title',)

    def __str__(self):
        return self.title

          
class Program(models.Model):
    title = models.CharField(max_length=75)
    location = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    artist = models.ManyToManyField('Artist', null=True, blank=True)
    secondary_artist = models.CharField(max_length=100, null=True, blank=True)
    songs = models.ManyToManyField('Song', null=False, blank=False)

