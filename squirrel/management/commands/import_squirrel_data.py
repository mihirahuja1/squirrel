import csv
from django.core.management import BaseCommand
from app.models import Question

class Command(BaseCommand):
     help = "Import squirrel data."

     def add_arguments(self, parser):
         parser.add_argument('csvfile', nargs='?', type=argparse.FileType('r'))

     def handle(self, *args, **options):
         squirrel_data = []
         sq = Squirrel.objects.get(name=homeroom)
         with options['csvfile'] as csvfile:
             reader = csv.DictReader(csvfile)
             for row in reader:
                 squirrel = Squirrel()
                 squirrel.Latitude = row.get('X')
                 squirrel.Longitude = row.get('Y')
                 squirrel.Uniqure_Squirrel_ID = row.get('Unique Squirrel ID')
                 squirrel.Shift = row.get('Shift')
                 squirrel.Date = row.get('Date')
                # squirrel.Hector_squirrel_Number = row.get('Hector Squirrel Number')
                 squirrel.Age = row.get('Age_Category')
                 squirrel.Primary_Fur_Color = row.get('Primary Fur Color')
                # squirrel.Combination_of_Primary_and_Highlight_Color = row.get('Combination of Primary and Highkight Color')
                 #squirrel.Color_notes = row.get('X')
                 squirrel.Location = row.get('Location')
                 #squirrel.Above_Ground_Sighter_Measurement = row.get('X')
                 squirrel.Specific_Location = row.get('Specific Location')
                 squirrel.Running = row.get('Running')
                 squirrel.Chasing = row.get('Chasing')
                 squirrel.Climing = row.get('Climing')
                 squirrel.Eating = row.get('Eating')
                 squirrel.Foraging = row.get('Foraging')
                 squirrel.Other_Activities = row.get('Other')
                 squirrel.Kuks = row.get('Kuks')
                 squirrel.Quaas = row.get('Quaas')
                 squirrel.Moans = row.get('Moans')
                 squirrel.Tail_flags = row.get('Tail flags')
                 squirrel.Tail_twitches = row.get('Tail twitches')
                 squirrel.Approaches = row.get('Approaches')
                 squirrel.Indifferent = row.get('Indifferent')
                 squirrel.Runs_from = row.get('Runs from')
                # squirrel.Other_Interactions = row.get('X')
                # squirrel.LatLong = row.get('X')
                

