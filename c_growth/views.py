from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    # A random dictionary because that's what Rango did
    #WWRD
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage':"Compound Growth works!"}


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'c_growth/index.html', context=context_dict)


def about(request):

    about_dict = {'aboutmessage':"Brews to more views!"}


    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'c_growth/about.html', context=about_dict)
