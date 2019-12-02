from django.shortcuts import render
from .models import Sightings

from django.http import HttpResponse

def sightings(request):
    all_sightings = Sightings.objects.all()
    context = {
            'all_sightings': all_sightings,
    }
    return render(request,'squirrel/sightings.html',context)

def sightings_details(request, unique_squirrel_id):
    squirrel = Sightings.objects.get(id=unique_squirrel_id)
    return HttpResponse(squirrel.unique_squirrel_id)
def sightings_add():
    :



# Create your views here.
