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
                 student_list.append(Student(name=row["Student Name"], studentidnum=row["School ID"], homeroom=hr))



