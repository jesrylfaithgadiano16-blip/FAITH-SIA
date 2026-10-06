from django import forms
from .models import PetCare


class PetCareForm(forms.ModelForm):
    class Meta:
        model = PetCare
        fields = [
            'pet_name',
            'pet_type',
            'breed',
            'age',
            'gender',
            'owner_name',
            'contact_number',
        ]