from django.shortcuts import render
from .models import Sightings

def sightings(request):
    all_squirrels = Sightings.objects.all()
    return render(request,'squirrel/sightings.html',locals())
# Create your views here.
