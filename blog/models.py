#-*- coding: utf-8 -*-

from django.db import models

class Article(models.Model): 
    title   = models.CharField(max_length=100)
    author  = models.CharField(max_length=42)
    content = models.TextField(null=True)
    date_publi = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publication date")
    date_modif = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Modification date")

    def __unicode__(self):
        return u"%s" % self.title 