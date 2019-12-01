from django.shortcuts import render
from .models import Squirrels

def sightings(request):
    all_squirrels = Squirrels.objects.all()
    return render(request,'squirrel/sightings.html',locals())
# Create your views here.
