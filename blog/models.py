#-*- coding: utf-8 -*-
from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.contrib.auth.models import User

class Article(models.Model): 
    title       = models.CharField(max_length=100)
    author      = models.ForeignKey(User, on_delete=models.PROTECT)
    content     = MarkdownxField(blank=True, default='')
    description = MarkdownxField(blank=True, default='')
    date_publi  = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publication date")
    date_modif  = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Modification date")

    def __unicode__(self):
        return u"%s" % self.title 

    def __str__(self): 
        return u"%s" % self.title
    
    def formatted_content(self):
        return markdownify(self.content)

    def formatted_description(self):
        return markdownify(self.description)
    