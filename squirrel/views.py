from django.shortcuts import render
from .models import Sightings

from django.http import HttpResponse

def sightings(request):
    all_sightings = Sightings.objects.all()
    context = {
            'all_sightings': all_sightings,
    }
    return render(request,'squirrel/sightings.html',context)
# Create your views here.
