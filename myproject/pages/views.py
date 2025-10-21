from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def home_view(request):
    context = {}
    if request.user.is_authenticated:
        context['username'] = request.user.username
        context['is_authenticated'] = True
    else:
        context['is_authenticated'] = False
    return render(request, 'home.html', context)

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def plants_view(request):
    return render(request, 'plants.html')

def faq_view(request):
    return render(request, 'faq.html')

def membersonly_view(request):
    return render(request, 'membersonly.html')

def signup_view(request):
    registered = False
    if request.method == "POST":
        user_form = (request.POST)
        custom_form = (request.POST)
        if user_form.is_valid() and custom_form.is_valid():
            user = user_form.save(commit=False)
            user.save()
            custom = custom_form.save(commit=False)
            custom.user = user
            custom.save()
            registered = True
            # Only use 'user' here, after assignment
        else:
            # Handle form errors
            pass
    else:
        user_form = ()
        custom_form = ()
    return render(request, 'signup.html', {
        'user_form': user_form,
        'custom_form': custom_form,
        'registered': registered
        # Don't reference 'user' here unless it's always assigned
    })






# Create your views here.
