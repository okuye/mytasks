from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def todolist(request):
    content = {
        'welcome_text': "Welcome From Jinja2.",
    }
    return render(request, 'todolist.html', content)


def contact(request):
    content = {
        'contact_text': "Welcome to the contact page.",
    }
    return render(request, 'contact.html', content)


def about(request):
    content = {
        'about_text': "Welcome to the about page.",
    }
    return render(request, 'about.html', content)
