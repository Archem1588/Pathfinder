from django.http import HttpResponse
from django.shortcuts import render
from bikeways.coordinates import getLats, getLngs


def home(request):
    #getPoints()
    #if request.is_ajax() or request.method == 'GET':
        #return render(request, 'Success')
    return render(request, 'templates/bikeways/home.html')
    #lat = getLngs()
    #return HttpResponse(lat, content_type='application/json')

# def admin(request):
#     return render(request, 'templates/bikeways/admin.html')

#def getPoints():
#    lat = getLngs()
#    return HttpResponse(lat, content_type='application/json')

def coord_test(request):
    lat = getLngs()
    return HttpResponse(lat, content_type='application/json')
