# -*- coding: utf-8 -*-
from django import forms
from .models import Project
from django.contrib.auth.models import User
from mdeditor.widgets import MDeditorWidget

class ProjectForm(forms.ModelForm):
    clear_picture = forms.BooleanField(initial=False, required=False)
    field_order   = ['image', 'clear_picture']

    class Meta:
        model   = Project
        exclude = ('author', )
        widgets = {
            'image': forms.FileInput(attrs=None), 
            'description': MDeditorWidget(attrs={'rows': 20}),
            'content': MDeditorWidget(attrs={'rows': 40}),
        }