from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cat, Toy
from .forms import FeedingForm, CatForm


# ----------------------- STATIC PAGES
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')


# ----------------------- CATS

def cats_index(request):
    cats = Cat.objects.all()

    return render(request, 'cats/index.html', { 'cats': cats })

def cats_detail(request, cat_id):
    cat = Cat.objects.get(id=cat_id)

    toys_cat_doesnt_have = Toy.objects.exclude(id__in=cat.toys.all().values_list('id'))

    feeding_form = FeedingForm()

    return render(request, 'cats/detail.html', {
        'cat': cat,
        'feeding_form': feeding_form,
        'toys': toys_cat_doesnt_have
    })


def add_cat(request):
    if request.method == 'POST':
        cat_form = CatForm(request.POST)
        if cat_form.is_valid():
            new_cat = cat_form.save()
            return redirect('detail', new_cat.id)
    else:
        form = CatForm()
        context = {'form': form}
        return render(request, 'cats/new.html', context)


def delete_cat(request, cat_id):
    Cat.objects.get(id=cat_id).delete()
    return redirect('cats_index')


def edit_cat(request, cat_id):
    cat = Cat.objects.get(id=cat_id)

    if request.method == 'POST':
        cat_form = CatForm(request.POST, instance=cat)
        if cat_form.is_valid():
            updated_cat = cat_form.save()
            return redirect('detail', updated_cat.id)
    else:
        form = CatForm(instance=cat)
        context = {'form': form, 'cat': cat}
        return render(request, 'cats/edit.html', context)

# ----------------------- CAT TOYS

def assoc_toy(request, cat_id, toy_id):
    # Find Cat by id
    cat = Cat.objects.get(id=cat_id)
    toy = Toy.objects.get(id=toy_id)
    cat.toys.add(toy)
    return redirect('detail', cat_id)


# ----------------------- CAT FEEDINGS

def add_feeding(request, cat_id):
    form = FeedingForm(request.POST)

    # if form is valid
    if form.is_valid():
        # submit the form
        new_form = form.save(commit=False)
        new_form.cat_id = cat_id
        new_form.save()

    return redirect('detail', cat_id)
    