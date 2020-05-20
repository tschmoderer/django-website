#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class Article(models.Model): 
    author      = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    title       = models.CharField(verbose_name='Article title',
                max_length=100, blank=True, default='Article Title',
                help_text='Set your article title')

    content     = models.TextField(verbose_name='Article content',
                blank=True, default='',
                help_text='Article content')

    description = models.TextField(verbose_name='Article description',
                blank=True, default='',
                help_text='Article description')

    date_publi  = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publication date")
    date_modif  = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Modification date")

    def __unicode__(self):
        return u"%s" % self.title 

    def __str__(self): 
        return u"%s" % self.title

    def get_absolute_url(self):
        return reverse('blog:read_article', kwargs={'pk': self.pk})