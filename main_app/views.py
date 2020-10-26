from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello from the home view!!!</h1>')

def about(request):
    return HttpResponse('<h1>All about the cat collector!!!</h1>')