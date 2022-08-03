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
    url = 'http://abzed-portfolio-api.herokuapp.com/projects'
    res = requests.get(url)
    projects = res.json()
    # projects = Code.objects.all()
    # images = Image.objects.filter(projects=projects)
    return render(request, 'project.html', {'title': title, 'projects' : projects})

def single_project(request, name):
    url = 'http://abzed-portfolio-api.herokuapp.com/projects?q={{name}}'
    res = requests.get(url)
    projects = res.json()
    title = name
    return render(request, 'single_project.html', {'title': title, 'projects' : projects})

def articles(request):
    title = "Articles"
    url = 'https://dev.to/api/articles?username=abzed'
    res = requests.get(url)
    data = res.json()
    return render(request, 'articles.html', {'title': title, 'data': data})


















