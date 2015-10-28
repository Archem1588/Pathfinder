from django.core.management.base import BaseCommand
from xml.etree.ElementTree import ElementTree
from bikeways.models import CoordinateData
import os
import django



class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):

        tree = ElementTree()
        data = tree.parse('bikeways.kml')
        coord = data.findall('.//{http://www.opengis.net/kml/2.2}coordinates')
        for i in coord:
            newList = i.text.split()

        item = newList[0]
        #for item in newList:
        lat = item[0:12]
        lng = item[18:30]
        c = CoordinateData(latitude=float(lat), longitude=float(lng))
        c.save()
        # For testing purposes
        print(float(lat))
        print(float(lng))

        # For testing purposes



    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epl.settings')
        django.setup()
        self._create_tags()
