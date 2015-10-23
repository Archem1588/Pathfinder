from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login

# Create your views here.
def map(request):
    return render(request, 'map/gmap.html')
