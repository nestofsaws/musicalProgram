from django.db import models
from django.utils import timezone

# Create your models here.
class Artist (models.Model):
    first_name = models.CharField(unique=False, max_length=50)
    last_name = models.CharField(unique=False, max_length=50)    
    artistid = models.CharField(unique = True, max_length=12)
    url = models.CharField(unique=True, max_length=200, null=True)
  
    class Meta(object):
        ordering = ('last_name', 'first_name')

    def __unicode__(self):
        return U'%s %s' %(self.last_name, self.id) 

class Song(models.Model):
    title = models.CharField(unique=True, max_length=50)
    key = models.CharField(unique=False, max_length=50, null=True)
    language = models.CharField(unique=False, max_length=50, null=True)
    date = models.CharField(unique=False, max_length=50, null=True)
    instrumentation = models.CharField(unique=False, max_length=50, null=True)
    description = models.CharField(max_length = 200, default='')
    composers = models.ManyToManyField('Artist')

    class Meta(object):
        verbose_name_plural = 'Songs'
        ordering = ('title', 'date')

    def __unicode__(self):
        return u'%s' % (self.title)
          
