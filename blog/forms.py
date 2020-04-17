# -*- coding:utf-8 -*-

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    field_order = ['title', 'description', 'content']
    class Meta:
        model   = Article
        exclude = ('author', )
