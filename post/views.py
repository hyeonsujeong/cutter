from .models import Post
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def csv(request):
    return render(request, 'csv.html')

def info(request):
    return render(request, 'info.html')

def conner(request):
    return render(request, 'conner.html')

def embellishment(request):
    return render(request, 'embellishment.html')

def manbox(request):
    return render(request, 'manbox.html')

def ending(request):
    return render(request, 'ending.html')