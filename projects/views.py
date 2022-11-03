from django.shortcuts import render

def blinderResume(request):
    return render(request, 'projects/blinder_resume.html')

def webMap(request):
    return render(request, 'projects/web_map.html')

def cryptoML(request):
    return render(request, 'projects/crypto_ml.html')

def bart(request):
    return render(request, 'projects/bart.html')