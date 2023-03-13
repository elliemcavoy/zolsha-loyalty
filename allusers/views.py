from django.shortcuts import render, get_object_or_404, redirect, reverse
from profiles.models import UserProfile
from django.db.models import Q
# Create your views here.

def all_users(request):
    """ View to render the menu page """

    users = UserProfile.objects.all()
    if request.GET:

       if 'q' in request.GET:
            query = request.GET['q']

            queries = Q(name__icontains=query)
        
            users = users.filter(queries)


    context = {
        'users': users,
    }
    return render(request, 'allusers/allusers.html', context)