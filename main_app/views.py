from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat
from .forms import FeedingForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cats_index(request):
    cats = Cat.objects.all()

    return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)

    feeding_form = FeedingForm()

    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form
    })

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)

    # if form is valid
    if form.is_valid():
        # submit the form
        new_form = form.save(commit=False)
        new_form.cat_id = cat_id
        new_form.save()

    return redirect('detail', cat_id=cat_id)
    