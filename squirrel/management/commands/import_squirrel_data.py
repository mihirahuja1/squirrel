rom django.core.management.base import BaseCommand
import pandas as pd
from tracker.models import Squirrel

class Command(BaseCommand):
    help = 'imports squirrel data from path'
    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        df = pd.read_csv(path)
        for index, row in df.iterrows():
            squirrel = Squirrel()
            squirrel.latitude = row['X']
            squirrel.longitude = row['Y']
            squirrel.unique_squirrel_id = row['Unique Squirrel ID']
            squirrel.shift = row['Shift']
            date = str(row['Date'])
            squirrel.date = f'{date[4:]}-{date[:2]}-{date[2:4]}'
            squirrel.age = row['Age']
            squirrel.primary_fur_color = row['Primary Fur Color']
            squirrel.location = row['Location']
            squirrel.specific_location = row['Specific Location']
            squirrel.running = row['Running']
            squirrel.chasing = row['Chasing']
            squirrel.climbing = row['Climbing']
            squirrel.eating = row['Eating']
            squirrel.foraging = row['Foraging']
            squirrel.other_activities = row['Other Activities']
            squirrel.kuks = row['Kuks']
            squirrel.quaas = row['Quaas']
            squirrel.moans = row['Moans']
            squirrel.tail_flags = row['Tail flags']
            squirrel.tail_twitches = row['Tail twitches']
            squirrel.approaches = row['Approaches']
            squirrel.indifferent = row['Indifferent']
            squirrel.runs_from = row['Runs from']
            squirrel.save()i




