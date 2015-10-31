from django.shortcuts import render


def home(request):
    return render(request, 'templates/bikeways/home.html')


def admin(request):
    return render(request, 'templates/bikeways/admin.html')