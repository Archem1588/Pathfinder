from django.http import HttpResponse
from django.shortcuts import render
from bikeways.coordinates import getCoords, getCoordsWithID
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'bikeways/home.html')


def coord_test(request):
    coord = getCoords()
    return HttpResponse(coord, content_type='application/json')


def coordwithid_test(request):
    coord = getCoordsWithID()
    return HttpResponse(coord, content_type='application/json')


def about(request):
    return render(request, "about.html", {})
