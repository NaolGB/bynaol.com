from django.shortcuts import render

def home(request):
    return render(request, 'projects/home.html')

def blinderResume(request):
    return render(request, 'projects/blinder_resume.html')