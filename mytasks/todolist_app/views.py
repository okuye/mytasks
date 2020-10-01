from django.shortcuts import render
from django.http import HttpResponse
from todolist_app.models import TaskList

# Create your views here.


def todolist(request):
    all_tasks = TaskList.objects.all

    return render(request, 'todolist.html', {'all_tasks' : all_tasks })


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
