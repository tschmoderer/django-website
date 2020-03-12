#-*- coding: utf-8 -*-

from django.db import models

class Homepage(models.Model): 
    title   = models.CharField(max_length=100)
    content = models.TextField(null=True)
    date_modif = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Modification date")

    def __unicode__(self):
        return u"%s" % self.title 