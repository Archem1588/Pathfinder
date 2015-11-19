from django.core.urlresolvers import reverse
from django.shortcuts import render  # Render a template back to browser
from django.http import HttpResponseRedirect # Redirect browser to different URLs
from accounts.forms import EditProfileForm


def show_profile(request):
    # return render_to_response('accounts/profile.html', {'full_name': request.user.username},
    #                           context_instance=RequestContext(request))

    user = request.user
    form = EditProfileForm(initial={'username': user.username,
                                    'first_name': user.first_name,
                                    'last_name': user.last_name,
                                    'email': user.email})
    context = {
        "form": form
    }
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):

    user = request.user
    form = EditProfileForm(request.POST or None, initial={'username': user.username,
                                                          'first_name': user.first_name,
                                                          'last_name': user.last_name,
                                                          'email': user.email})
    if request.method == 'POST':
        if form.is_valid():

            user.username = request.POST['username']
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()
            return HttpResponseRedirect('%s'%(reverse('profile')))

    context = {
        "form": form
    }

    return render(request, "accounts/edit_profile.html", context)


