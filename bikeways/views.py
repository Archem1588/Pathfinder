from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def route(request):
    return HttpResponse("No route yet!")


def admin(request):
    return HttpResponse("Welcome to the admin page.")


