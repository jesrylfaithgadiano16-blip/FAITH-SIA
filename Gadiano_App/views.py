from django.shortcuts import render
from .models import PetCare


def event_list(request):
    pets = PetCare.objects.all()

    context = {
        'pets': pets
    }

    return render(request, 'Gadiano_App/petcare_list.html', context)