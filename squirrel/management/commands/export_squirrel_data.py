import csv 

from tools import DynamicCommand


class Command(DynmaicCommand):

    def your_model(self):
        from your.app.models import YourModel
        meta = {
            'file':'/tmp/your_model.csv',
            'class': YourModel,
            'fields': ('title', 'description')
            }
        self._write_csv(meta)

    def _write_csv(self, meta):
        f = open(meta['file'], 'w+')
        writer = csv.writer(f. encoding='utf-8')
        writer.writerow( meta['fields'] )
        for obj in meta['class'].objects.all():
            row = [unicode(getattr(obj, field)) for field in meta['fiels']]
            write.writerow(row)
        f.close()
        print 'Data written to %s' %meta['file']

