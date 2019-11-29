from django.db import models

from django.utils.translation import gettext as _

class Pet(models.Model):
    species = models.CharField(
            max_length=100,
            help_text=_('Species of pet'),
        )
    birth_date = models.DateField(
            help_text=_('Bday of pet'),
    )

    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'
    
    SEX_CHOICES = (
            (MALE, 'Male'),
            (FEMALE, 'Female'),
            (OTHER, 'Other'),
            )


    sex = models.CharField(
            max_length=16,
            choices=SEX_CHOICES,
            default=OTHER,
            )

    def __str__(self):
        return self.species

# Create your models here.
