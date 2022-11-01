from django.shortcuts import render
from projects.models import Project

def home(request):
    context = {
        'projects' : Project.objects.all()
    }

    return render(request, 'home/home.html', context=context)

def about(request):
    return render(request, 'home/about.html')