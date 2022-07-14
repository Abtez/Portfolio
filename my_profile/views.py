from django.shortcuts import render

def home(request):
    title = 'Home'
    return render(request, 'index.html', {'title': title})

def social(request):
    title = 'Social Platform'
    return render(request, 'social.html', {'title': title})

def profile(request):
    title = "Abzed's Profile"
    return render(request, 'about.html', {'title': title})


















