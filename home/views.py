from django.shortcuts import render
from django.http import HttpResponse

def home(reques):
    return HttpResponse('Hi, just putting last touches. Come back a little later 🙂.')