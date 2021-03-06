from django.core.management.base import BaseCommand
from squirrel.models import Sightings
import csv

class Command(BaseCommand):
    help = 'export of squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        
    def handle(self, *args, **options):
        path = options['path']
        sightings = Sightings.objects.all()
        fields = [field.name for field in Sightings._meta.fields]
        with open(path, mode='w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(fields)
            for sighting in sightings:
                writer.writerow([getattr(sighting, field) for field in fields])