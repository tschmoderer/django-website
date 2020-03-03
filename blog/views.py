#-*- coding: utf-8 -*-
from django.shortcuts import render

from datetime import datetime

def home(request):
	return render(request, 'blog/tpl.html', {'current_date':datetime.now()})
