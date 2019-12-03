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
        form = Add(request.POST)
        
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
