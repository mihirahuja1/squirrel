import csv

from django.core.management.base import BaseCommand, CommandError
import csv
import sys

class Command(BaseCommand):
    help = ("Output the specified model as CSV")
    args = '[appname.ModelName]'

    def handle(self, *args, **kwargs):
        from django.db.models import get_model
        squirrel, Sightings = args[0].split('.')
        model = get_model(squirrel, Sightings)
        field_names = [f.name for f in model._meta.fields]
        writer = csv.writer(sys.stdout, quoting=csv.QUOTE_ALL)
        writer.writerow(field_names)
        for instance in model.objects.all():
            writer.writerow([unicode(getattr(instance, f)).encode('utf-8') for f in field_name


