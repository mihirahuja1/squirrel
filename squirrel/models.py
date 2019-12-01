from django.db import models


from django.db import models
from django.utils.translation import gettext as _

class Squirrel(models.Model):
    X = models.FloatField(
            help_text=_('Latitude'),
            )
    
    Y = models.FloatField(
            help_text=_('Longitude'),
            )
    Unique_Squirrel_ID = models.CharField(
            help_text=_('Unique Squirrel id'),
            max_length=50,
            )
    Shift = models.CharField(
            help_text=_('Shift'),
            max_length=100,
            )

    Date = models.DateField(
            help_text=_('Date'),
            )

    Hectare_Squirrel_Number = models.IntegerField(
            help_text=_('Hectare Squirrel Number'),
            )

    Age = models.CharField(
            help_text=_('Age category'),
            max_length=100,
            )
    Highlight_Fur_Color = models.CharField(
         max_length=200,
            )
    Combination_of_Primary_and_Highlight_Color= models.CharField(
            max_length=200,
            )
    Color_notes = models.CharField(
            max_length=200,
            )
    Location = models.CharField(
            max_length=200,
            )
    Above_Ground_Sighter_Measurement = models.CharField(
            max_length=200,
            )
    Specific_Location = models.CharField(
            max_length=200,
            )
    Running = models.BooleanField()
    Chasing = models.BooleanField()
    Climbing = models.BooleanField()
    Eating = models.BooleanField()
    Foraging = models.BooleanField()
    Other = models.CharField( 
            max_length=200,
            )
    Kuks = models.BooleanField()
    Quaas = models.BooleanField()
    Moans = models.BooleanField()
    Tail_flags = models.BooleanField()
    Tail_twitches = models.BooleanField()
    Approaches = models.BooleanField()
    Indifferent = models.BooleanField()
    Runs_from = models.BooleanField()
    Other_Interactions = models.CharField(
            max_length=200,
            )
    LatLong = models.CharField(
            max_length=200,
            )


# Create your models here.
