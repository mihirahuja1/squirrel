from django.shortcuts import render
from .models import Sightings
from .forms import Add

from django.http import HttpResponse

def sightings(request):
    all_sightings = Sightings.objects.all()
    context = {
            'all_sightings': all_sightings,
    }
    return render(request,'sightings/sightings.html',context)

def sightings_details(request, unique_squirrel_id):
    squirrel = Sightings.objects.get(id=unique_squirrel_id)
    return HttpResponse(squirrel.unique_squirrel_id)
def sightings_add(request):
    if request.method == 'POST':
        #form = Add(request.POST)
        new_data = Sightings()
        #new_data.title = request.POST.get('title')

        new_data.latitude = request.POST.get('latitude')
        new_data.longitude = request.POST.get('longitude')
        new_data.unique_squirrel_id = request.POST.get('unique_squirrel_id')
        new_data.shift = request.POST.get('shift')
        new_data.date = request.POST.get('date')
        new_data.age = request.POST.get('age')
        new_data.primary_fur_color = request.POST.get('primary_fur_color')
        new_data.location  = request.POST.get('location')
        new_data.specific_location  = request.POST.get('specific_location')
        new_data.running = request.POST.get('running')
        new_data.chasing = request.POST.get('chasing')
        new_data.climbing = request.POST.get('climbing')
        new_data.eating = request.POST.get('chasing')
        new_data.foraging = request.POST.get('eating')
        new_data.other_activities = request.POST.get('foraging')
        new_data.kuks = request.POST.get('kuks')
        new_data.quaas = request.POST.get('quaas')
        new_data.moans = request.POST.get('moans')
        new_data.tail_flags = request.POST.get('tail_flags')
        new_data.tail_twitches = request.POST.get('tail_twitches')
        new_data.approaches = request.POST.get('approaches')
        new_data.indifferent = request.POST.get('indifferent')
        new_data.runs_from = request.POST.get('runs_from')





        
    else:
        form = Add()
    return render(request,'sightings/add.html',{'form':form})
def sightings_stats(request):
    all_sightings = Sightings.objects.all()
    #context = {
    #        'all_sightings': all_sightings,
    #}
    return render(request,'sightings/stats.html',context)
def map(request):
    return render(request,'map.html',context)
    



# Create your views here.
