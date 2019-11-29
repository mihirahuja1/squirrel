import csv
from django.core.management import BaseCommand
from squirrel.models import Squirrel
import pandas as pd

class Command(BaseCommand):
     help = "Import squirrel data."

     def add_arguments(self, parser):
         parser.add_argument('csv_file', nargs='+', type=str)
    
    def handle(self, *args, **kwargs):
         csv_file = args['csv_file']
         dataReader = pd.read_csv(csv_file, encoding = 'latin1')
         for index, row in dataReader.iterrows():

    # def handle(self, *args, **options):
     #    for csv_file in options['csv_file']:
      #       dataReader = pd.read_csv('csv_file', encoding = 'latin1')
       #      for index, row in dataReader.iterrows():
                 squirrel = Squirrel()
                 squirrel.Latitude = row['X']
                 squirrel.Longitude = row['Y']
                 squirrel.Uniqure_Squirrel_ID = row['Unique Squirrel ID']
                 squirrel.Shift = row['Shift']
                 squirrel.Date = row['Date']
                 # squirrel.Hector_squirrel_Number = row.get('Hector Squirrel Number')
                 squirrel.Age = row['Age_Category']
                 squirrel.Primary_Fur_Color = row['Primary Fur Color']
                  # squirrel.Combination_of_Primary_and_Highlight_Color = row.get('Combination of Primary and Highkight Color')
                 #squirrel.Color_notes = row.get('X')
                 squirrel.Location = row['Location']
                 #squirrel.Above_Ground_Sighter_Measurement = row.get('X')
                 squirrel.Specific_Location = row['Specific Location']
                 squirrel.Running = row['Running']
                 squirrel.Chasing = row['Chasing']
                 squirrel.Climing = row['Climing']
                 squirrel.Eating = row['Eating']
                 squirrel.Foraging = row['Foraging']
                 squirrel.Other_Activities = row['Other']
                 squirrel.Kuks = row['Kuks']
                 squirrel.Quaas = row['Quaas']
                 squirrel.Moans = row['Moans']
                 squirrel.Tail_flags = row['Tail flags']
                 squirrel.Tail_twitches = row['Tail twitches']
                 squirrel.Approaches = row['Approaches']
                 squirrel.Indifferent = row['Indifferent']
                 squirrel.Runs_from = row['Runs from']
                # squirrel.Other_Interactions = row.get('X')
                # squirrel.LatLong = row.get('X')
                 squirrel.save() 

