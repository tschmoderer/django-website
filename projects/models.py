#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
import os

def upload_project_pict(instance, filename):
    ext = filename.split('.')[-1]
    return os.path.join('projects', instance.author.username, 'projects', instance.title + '-project-picture' + '.' + ext )


class Project(models.Model): 
    author      = models.ForeignKey(User, to_field='id', on_delete=models.CASCADE)
    title       = models.CharField(verbose_name='Project title',
                max_length=100, blank=True, default='Project Title',
                help_text='Set your project title')

    link        = models.CharField(verbose_name='Project url', 
                max_length=200, blank=True, default='example.org', 
                help_text='Set your project url')

    image       = models.ImageField(verbose_name='Project image', 
                upload_to=upload_project_pict, blank=True, null=True)


    description = models.TextField(verbose_name='Project description',
                blank=True, default='',
                help_text='Project description')

    date_publi  = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Publication date")
    date_modif  = models.DateTimeField(auto_now_add=False, auto_now=True, verbose_name="Modification date")

    @property
    def image_url(self):
        if self.image:
            return self.image.url
        else:
            return "/static/projects/img/default-projet.png"
    
    @property
    def get_link(self): 
        return 'projects:' + self.link

    def __unicode__(self):
        return u"%s" % self.title 

    def __str__(self): 
        return u"%s" % self.title

    # def get_absolute_url(self):
    #    return reverse('blog:read_article', kwargs={'pk': self.pk})