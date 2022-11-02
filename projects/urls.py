from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects_home'),
    path('blinder_resume/', views.blinderResume, name='projects_blinder_resume'),
]
