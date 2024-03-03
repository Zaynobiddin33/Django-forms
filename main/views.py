from django.shortcuts import render, redirect
from .forms import *

# Create your views here.

def index(request):
    form = PersonForm()
    context = {'form': form}
    if request.method == 'POST':
        data = Person.objects.create(
            name = request.POST['name'],
            surname = request.POST['surname'],
            age = request.POST['age'],
        )
        return redirect('enter', data.id)
    return render(request, 'index.html', context)

def enter(request, id):
    person =  Person.objects.get(id = id)
    context = {'person': person}
    return render(request, 'second.html', context)