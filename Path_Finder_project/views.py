from django.http import HttpResponse
from django.shortcuts import render
from bikeways.coordinates import getCoords
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'bikeways/home.html')

def coord_test(request):
    coord = getCoords()
    #return HttpResponse(coord, content_type='application/json')
    return HttpResponse("hello")
