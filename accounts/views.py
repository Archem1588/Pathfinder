from django.shortcuts import render_to_response # Render a template back to browser
from django.http import HttpResponseRedirect # Redirect browser to different URLs
from django.contrib import auth # Check username and password/ confirmation
from django.core.context_processors import csrf # Protection from hackers

# Create your views here.

def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('accounts/login.html', c)

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/accounts/loggedin')
    else:
        # Have not found the user
        return HttpResponseRedirect('/accounts/invalid')

def loggedin(request):
    return render_to_response('accounts/loggedin.html', {'full_name': request.user.username})

def invalid_login(request):
    return render_to_response('accounts/invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('accounts/logout.html')