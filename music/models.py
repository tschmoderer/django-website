from django.db import models

class MusicPicture(models.Model): 
    title       = models.CharField(max_length=100, default='')
    filename    = models.ImageField(upload_to='music/images/', default='')
    date_publi  = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publication date")

class DBMusic(models.Model):
    title    = models.CharField(max_length=100, default='')
    picture  = models.ForeignKey(MusicPicture, on_delete=models.PROTECT,default='', null=True)
    filename = models.FileField(upload_to = 'music/databases/',default='') 

    def __unicode__(self):
        return self.title