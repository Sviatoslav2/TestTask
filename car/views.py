from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils import timezone

from .form import CarForm
from .models import Car

def post_list(request):
    cars = Car.objects.order_by('category')
    ctx = {'cars': cars}
    return render(request, 'cars/carslist.html', ctx)


def car_list(request, sort_method):
    cars = Car.objects.order_by(sort_method)
    ctx = {'cars': cars}
    return render(request, 'cars/carslist.html', ctx)

def add_car(request):
    if request.method == "POST":
        form = CarForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = CarForm()

    return render(request,'cars/add_car.html',{'form': form})