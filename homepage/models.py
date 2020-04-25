#-*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
import os

def upload_profil_pict(instance, filename):
    upload_to = 'profile'
    ext = filename.split('.')[-1]
    return os.path.join(instance.user.username, upload_to, instance.user.username + '-profile-picture' + '.' + ext )

class Homepage(models.Model): 
    user    = models.OneToOneField(User, to_field='id', primary_key=True, on_delete=models.CASCADE)
    title   = models.CharField(verbose_name='Homepage title',
            max_length=100, blank=True, default='Homepage',
            help_text="Set your homepage title")

    content = models.TextField(verbose_name="Homepage content",
            blank=True, default='Welcome on my Homepage',
            help_text="Enter your homepage content. Markdown and/or html syntax are accepted")

    def __unicode__(self):
        return u"%s" % self.title 

    def __str__(self):
        return u"%s" % self.title

class Profile(models.Model):
    user        = models.OneToOneField(User, to_field='id', primary_key=True, on_delete=models.CASCADE)
    picture     = models.ImageField(verbose_name='Profile picture', upload_to=upload_profil_pict, blank=True, default='profile/default-profil.jpg')
    
    description = models.CharField(verbose_name='Short description',               
                max_length=150, 
                blank=True, 
                default='', 
                help_text="A short description of your position")

    place       = models.CharField(verbose_name='Place',                     
                max_length=150, blank=True, default='', 
                help_text="Your working place")

    twitter     = models.CharField(verbose_name='Twitter username',         
                max_length=30, blank=True, default='', 
                help_text="Your Twitter username: https://twitter.com/<username>")

    github      = models.CharField(verbose_name='Github username',          
                max_length=30, blank=True, default='', 
                help_text="Your Github username: https://github.com/<username>")

    linkedin    = models.CharField(verbose_name='Linkedin id',        
                max_length=30, blank=True, default='',
                help_text="Indicate your Linkedin id: https://www.linkedin.com/in/<id>")

    youtube     = models.CharField(verbose_name='Youtube channel id',         
                max_length=30,  
                blank=True, 
                default='',
                help_text="Indicate your youtube channel id: https://www.youtube.com/channel/<id>")

    scholar     = models.CharField(verbose_name='Google scholar id',  
                max_length=30,  
                blank=True, 
                default='',
                help_text="Indicate you google scholar id: https://scholar.google.com/citations?user=<id>")
    
    orcid       = models.CharField(verbose_name='OrcId',           
                max_length=20,  
                blank=True, 
                default='', 
                help_text="Indicate your OrcId: https://orcid.org/<0000-0000-0000-000>")
    
    lichess     = models.CharField(verbose_name='Lichess username',         
                max_length=30,  
                blank=True, 
                default='', 
                help_text="Indicate your Lichess username: https://lichess.org/@/<username>")

    def __str__(self):
        return u"%s" % self.user.username
    
    def __unicode__(self):
        return u"%s" % self.user.username

    def get_twitter_link(self): 
        return "https://twitter.com/{0}".format(self.twitter)

    def get_github_link(self): 
        return "https://github.com/{0}".format(self.github)

    def get_linkedin_link(self):
        return "https://www.linkedin.com/in/{0}".format(self.linkedin)

    def get_youtube_link(self):
        return "https://www.youtube.com/channel/{0}".format(self.youtube)
    
    def get_scholar_link(self): 
        return "https://scholar.google.com/citations?user={0}".format(self.scholar)
    
    def get_orcid_link(self): 
        return "https://orcid.org/{0}".format(self.orcid)
    
    def get_lichess_link(self): 
        return "https://lichess.org/@/{0}".format(self.lichess)