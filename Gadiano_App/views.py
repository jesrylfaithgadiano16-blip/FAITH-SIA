from django.shortcuts import render, redirect, get_object_or_404
from .models import PetCare
from .forms import PetCareForm


def event_list(request):
    pets = PetCare.objects.all()
    return render(request, 'Gadiano_App/petcare_list.html', {'pets': pets})


def add_pet(request):
    if request.method == 'POST':
        form = PetCareForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = PetCareForm()

    return render(request, 'Gadiano_App/add_pet.html', {'form': form})


def delete_pet(request, pet_id):
    if request.method == 'POST':
        pet = get_object_or_404(PetCare, pet_id=pet_id)
        pet.delete()

    return redirect('event_list')