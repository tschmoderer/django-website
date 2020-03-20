#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from datetime import date
import os

def upload_profil_pict(instance, filename):
    upload_to = 'profil'
    ext = filename.split('.')[-1]
    return os.path.join(upload_to, instance.user.username + '-profil' + '.' + ext )


class Homepage(models.Model): 
    user       = models.OneToOneField(User, on_delete=models.PROTECT)
    title      = models.CharField(max_length=100, default='')
    content    = MarkdownxField(blank=True, default='')

    def __unicode__(self):
        return u"%s" % self.title 

    def __str__(self):
        return u"%s" % self.title
    
    def formatted_content(self): 
        return markdownify(self.content)

class Profile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.PROTECT)
    picture     = models.ImageField(verbose_name='profil picture', upload_to=upload_profil_pict, blank=True, default='profil/default-profil.jpg')
    description = models.CharField(verbose_name='description',               max_length=150, blank=True, default='')
    place       = models.CharField(verbose_name='place',                     max_length=150, blank=True, default='')
    twitter     = models.CharField(verbose_name='twitter user name',         max_length=30,  blank=True, default='')
    github      = models.CharField(verbose_name='github user name',          max_length=30,  blank=True, default='')
    linkedin    = models.CharField(verbose_name='linkedin user name',        max_length=30,  blank=True, default='')
    youtube     = models.CharField(verbose_name='youtube user name',         max_length=30,  blank=True, default='')
    scholar     = models.CharField(verbose_name='google scholar user name',  max_length=30,  blank=True, default='')
    orcid       = models.CharField(verbose_name='orcid user name',           max_length=30,  blank=True, default='')
    arxiv       = models.CharField(verbose_name='arxiv user name',           max_length=30,  blank=True, default='')
    lichess     = models.CharField(verbose_name='lichess user name',         max_length=30,  blank=True, default='')

    def __str__(self):
        return u"%s" % self.user.username
    
    def __unicode__(self):
        return u"%s" % self.user.username
