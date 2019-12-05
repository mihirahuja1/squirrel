from django.shortcuts import render, redirect
from .models import Sightings
from .forms import SightingsForm
from django.core.exceptions import MultipleObjectsReturned


from django.http import HttpResponse

def sightings(request):
    all_sightings = Sightings.objects.all()
    context = {
            'all_sightings': all_sightings,
    }
    return render(request,'sightings/sightings.html',context)

def sightings_add(request):
    if request.method == 'POST':
        form = SightingsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightingsForm()
    context = { 
        'form' : form, 
    }
    return render(request, 'sightings/edit.html', context)

def sightings_edit(request, unique_squirrel_id):
    squirrel = Sightings.objects.filter(unique_squirrel_id=unique_squirrel_id).first()
    if request.method == 'POST':
        form = SightingsForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/sightings/')
    else:
        form = SightingsForm(instance=squirrel)
    context = { 
        'form' : form, 
    }
    return render(request, 'sightings/edit.html', context)


def sightings_stats(request):
    all_sightings = Sightings.objects.all()
    #context = {
    #        'all_sightings': all_sightings,
    #}
    return render(request,'sightings/stats.html',context)

def map(request):
    all_sightings = Sightings.objects.all()[:100]
    context = {
            'all_sightings': all_sightings,
    }
    return render(request,'sightings/map.html',context)

    

# Create your views here.
