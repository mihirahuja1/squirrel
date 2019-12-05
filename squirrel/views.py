from django.shortcuts import render, redirect
from .models import Sightings
from .forms import SightingsForm
from django.core.exceptions import MultipleObjectsReturned
from django.db.models import Count


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

def sightings_stats(request):
    squirrel_age = Sightings.objects.values('age').order_by('age').annotate(age_count=Count('age'))
    squirrel_primary_fur_color = Sightings.objects.values('primary_fur_color').order_by('primary_fur_color').annotate(primaryfurcolor_count=Count('primary_fur_color'))
    squirrel_climbing =  Sightings.objects.values('climbing').order_by('climbing').annotate(climbing_count=Count('climbing'))
    squirrel_chasing = Sightings.objects.values('chasing').order_by('chasing').annotate(chasing_count=Count('chasing'))
    squirrel_running = Sightings.objects.values('running').order_by('running').annotate(running_count=Count('running'))
    context = {
        'squirrel_age': squirrel_age,
        'squirrel_primary_fur_color': squirrel_primary_fur_color,
        'squirrel_climbing': squirrel_climbing,
        'squirrel_chasing': squirrel_chasing,
        'squirrel_running': squirrel_running,
    }
    return render(request, 'sightings/stats.html', context)

def map(request):
    all_sightings = Sightings.objects.all()[:100]
    context = {
            'all_sightings': all_sightings,
    }
    return render(request,'sightings/map.html',context)

    

# Create your views here.
