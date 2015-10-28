__author__ = 'hannahpark'

from django.shortcuts import render

def home(request):
    return render(request, 'Sample/home.html')