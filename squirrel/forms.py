from django import forms

class Add(forms.Form):
    TRUE_FALSE_CHOICES = (
        (True, 'Yes'),
        (False, 'No'))
    latitude = forms.FloatField()
    longitude = forms.FloatField()
    unique_squirrel_id = forms.CharField(max_length=100)
    shift = forms.CharField(max_length=20)
    date = forms.DateField()
    age = forms.CharField(max_length=20)
    primary_fur_color = forms.CharField(max_length=200)
    location  = forms.CharField(max_length=200)
    specific_location  = forms.CharField(max_length=200)
    running = forms.CharField(max_length=100)
    chasing = forms.CharField(max_length=100)
    climbing = forms.CharField(max_length=100)
    eating = forms.CharField(max_length=100)
    foraging = forms.CharField(max_length=100)
    other_activities = forms.CharField(max_length=100)
    kuks = forms.CharField(max_length=100)
    quaas = forms.CharField(max_length=100)
    moans = forms.CharField(max_length=100)
    tail_flags = forms.CharField(max_length=100)
    tail_twitches = forms.CharField(max_length=100)
    approaches = forms.CharField(max_length=100)
    indifferent = forms.CharField(max_length=100)
    runs_from = forms.CharField(max_length=100)

