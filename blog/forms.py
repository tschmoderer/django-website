# -*- coding: utf-8 -*-
from django import forms
from .models import Article
from django.contrib.auth.models import User
from mdeditor.widgets import MDeditorWidget

class ArticleForm(forms.ModelForm):
    class Meta:
        model   = Article
        exclude = ('author', )
        widgets = {
            'description': MDeditorWidget(attrs={'rows': 20}),
            'content': MDeditorWidget(attrs={'rows': 40}),
        }