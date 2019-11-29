from django.http import HttpResponse
from .models import Pet

def all_pets(request):
    pets = Pet.object.all()
    context = {
            'pets':pets,
            }
    return render(request, 'adopt/all.html', context)

def pet_details(request, pet_id):
    pet = Pet.objects.get(id=pet_id)
    return HttpResponse(f"Hi, Im pet {pet.id}")
# Create your views here.
