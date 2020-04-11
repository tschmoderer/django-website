from django.db import models

class DBMusic(models.Model):
    title    = models.CharField(max_length=100, default='')
    filename = models.FileField(upload_to = 'music/databases/',default='') 

    def __unicode__(self):
        return self.title

    def get_filename(self): 
        return '/media/' + str(self.filename)
