from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from .models import *
import requests

def home(request):
    title = 'Home'
    return render(request, 'index.html', {'title': title})


def profile(request):
    title = "Abzed's Profile"
    return render(request, 'about.html', {'title': title})

def projects(request):
    title = "Projects"
    projects = Code.objects.all()
    images = Image.objects.filter(projects=projects)
    return render(request, 'project.html', {'title': title, 'projects' : projects, 'images': images})

def single_project(request, name):
    title = name
    project = get_object_or_404(Code, title=name)
    images = Image.objects.filter(projects=project)
    return render(request, 'single_project.html', {'title': title, 'projects' : project, 'images': images})

def articles(request):
    title = "Articles"
    url = 'https://dev.to/api/articles?username=abzed'
    res = requests.get(url)
    data = res.json()
    return render(request, 'articles.html', {'title': title, 'data': data})


















