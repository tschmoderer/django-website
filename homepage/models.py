#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models

class Homepage(models.Model): 
    user       = models.ForeignKey(User, on_delete=models.PROTECT)
    title      = models.CharField(max_length=100)
    content    = models.TextField(null=True)
    date_modif = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Modification date")

    def __unicode__(self):
        return u"%s" % self.title 

    def __str__(self):
        return u"%s" % self.title

class Profile(models.Model):
    user       = models.ForeignKey(User, on_delete=models.PROTECT)
    email      = models.EmailField(verbose_name='email address', max_length=255, unique=True)

    first_name = models.CharField(verbose_name='first name', max_length=30,  blank=True)
    last_name  = models.CharField(verbose_name='last name',  max_length=150, blank=True)

    place      = models.CharField(verbose_name='place',  max_length=150, blank=True)

    twitter    = models.CharField(verbose_name='twitter user name',  max_length=30, blank=True)
    github     = models.CharField(verbose_name='github user name',  max_length=30, blank=True)
    linkedin   = models.CharField(verbose_name='linkedin user name',  max_length=30, blank=True)
    youtube    = models.CharField(verbose_name='youtube user name',  max_length=30, blank=True)
    scholar    = models.CharField(verbose_name='google scholar user name',  max_length=30, blank=True)
    orcid      = models.CharField(verbose_name='orcid user name',  max_length=30, blank=True)
    arxiv      = models.CharField(verbose_name='arxiv user name',  max_length=30, blank=True)
    lichess    = models.CharField(verbose_name='lichess user name',  max_length=30, blank=True)

    def __str__(self):
        return u"%s" % self.pseudo
    
    def _get_unique_checks(self):
        return u"%s" % self.pseudo
