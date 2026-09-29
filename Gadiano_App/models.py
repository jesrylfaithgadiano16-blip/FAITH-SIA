from django.db import models


class PetCare(models.Model):
    pet_id = models.AutoField(primary_key=True)
    pet_name = models.CharField(max_length=100)
    pet_type = models.CharField(max_length=50)
    breed = models.CharField(max_length=100)
    age = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    owner_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.pet_name