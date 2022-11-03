from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects_home'),
    path('blinder_resume/', views.blinderResume, name='projects_blinder_resume'),
    path('web_map/', views.webMap, name='projects_web_map'),
    path('crypto_ml/', views.cryptoML, name='projects_crypto_ml'),
    path('bart/', views.bart, name='projects_bart'),
]
