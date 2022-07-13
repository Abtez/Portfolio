from django.shortcuts import render

def home(requests):
    title = 'Home'
    return render(requests, 'index.html', {'title': title})
