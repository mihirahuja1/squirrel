import csv
from django.core.management import BaseCommand
from squirrel.models import Squirrel
import pandas as pd

class Command(BaseCommand):
     help = "Import squirrel data."

     def add_arguments(self, parser):
         parser.add_argument('path' , type=str)
    
     def handle(self, *args, **kwargs):
         path = kwargs['path']
         df = pd.read_csv(path)
         for index, row in df.iterrows():
             squirrel = Squirrel()
             squirrel.Latitude = row['X']
             squirrel.Longitude = row['Y']
             squirrel.Uniqure_Squirrel_ID = row['Unique Squirrel ID']
             squirrel.Shift = row['Shift']
             date =str(row['Date']
                     squirrel.Date = f'{date[4:]}-{date[2]}-{date[2:4]}'
             squirrel.Age = row['Age_Category']
             squirrel.Primary_Fur_Color = row['Primary Fur Color']
             squirrel.Location = row['Location']
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
             squirrel.save() 
 
