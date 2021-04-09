from django.shortcuts import render, redirect
from . models import Dojo, Ninja

def main(request):
    all_dojo = Dojo.objects.all()
    all_ninja = Ninja.objects.all()
    context = {
    "all_dojo": all_dojo,
    "all_ninja": all_ninja,
    }
    return render(request, 'main.html', context)

def add_dojo(request):
    Dojo.objects.create(
    name=request.POST['name'], 
    city=request.POST['city'], 
    state=request.POST['state']
    )
    return redirect('/')

def add_ninja(request):
    Ninja.objects.create(
    first_name=request.POST['first_name'], 
    last_name=request.POST['last_name'],
    dojo=Dojo.objects.get(id=request.POST['dojo'])
    )
    return redirect('/')
