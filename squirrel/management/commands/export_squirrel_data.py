from django.core.management.base import BaseCommand
from tracker.models import Sighting
import csv
class Command(BaseCommand):
    help = 'export of squirrel data'

    def add_arguments(self, parser):
        parser.add_argument('path', type=str)
        
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        sightings = Sighting.objects.all()
        fields = [field.name for field in Sighting._meta.fields]
        with open(path, mode='w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(fields)
            for sighting in sightings:
                writer.writerow([getattr(sighting, field) for field in fields])