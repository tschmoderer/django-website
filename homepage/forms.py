# -*- coding: utf-8 -*-
from django import forms
from .models import Homepage, Profile
from django.contrib.auth.models import User
from mdeditor.widgets import MDeditorWidget

class UserForm(forms.ModelForm): 
    class Meta: 
        model  = User
        fields = ('first_name', 'last_name', 'email', )

class HomepageForm(forms.ModelForm):
    class Meta:
        model   = Homepage
        exclude = ('user', )
        widgets = {
            'content': MDeditorWidget(attrs={'rows': 40}),
        }

class ProfileForm(forms.ModelForm):
    clear_picture = forms.BooleanField(initial=False, required=False)
    field_order   = ['picture', 'clear_picture']

    # TODO: change label and help text 
    class Meta:
        model   = Profile
        widgets = {
            'picture': forms.FileInput(attrs=None)
        }
        exclude = ('user', )