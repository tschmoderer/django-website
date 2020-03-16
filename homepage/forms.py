# -*- coding: utf-8 -*-
from django import forms
from .models import Homepage, Profile

class HomepageForm(forms.ModelForm):
    class Meta:
        model   = Homepage
        exclude = ('user', )

class ProfileForm(forms.ModelForm):
    class Meta:
        model   = Profile
        exclude = ('user', )