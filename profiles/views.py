from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


def profile(request, user):
    """ Display the user's profile. """

    uprofile = get_object_or_404(UserProfile, user=user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=uprofile)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile updated successfully')

    form = UserProfileForm(instance=uprofile)
    

    template = 'profiles/profiles.html'
    context = {
        'profile': uprofile,
        'form': form,
    }

    return render(request, template, context)

