from django.db import models



class Sightings(models.Model):
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    unique_squirrel_id = models.CharField(max_length=100)
    shift = models.CharField(max_length=20)
    date = models.DateField(null=True)
    age = models.CharField(max_length=20)
    primary_fur_color = models.CharField(max_length=200)
    location  = models.CharField(max_length=200)
    specific_location  = models.CharField(max_length=200)
    running = models.BooleanField(null=True)
    chasing = models.BooleanField(null=True)
    climbing = models.BooleanField(null=True)
    eating = models.BooleanField(null=True)
    foraging = models.BooleanField(null=True)
    other_activities = models.CharField(max_length=200)
    kuks = models.BooleanField(null=True)
    quaas = models.BooleanField(null=True)
    moans = models.BooleanField(null=True)
    tail_flags = models.BooleanField(null=True)
    tail_twitches = models.BooleanField(null=True)
    approaches = models.BooleanField(null=True)
    indifferent = models.BooleanField(null=True)
    runs_from = models.BooleanField(null=True)

# Create your models here.
