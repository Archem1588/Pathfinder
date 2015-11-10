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
        multiGeom = data.findall('.//{http://www.opengis.net/kml/2.2}MultiGeometry')

        for item in multiGeom:
            for lineString in item:
                for coord in lineString:
                    lng = coord.text[0:12]  #Correct lat and lng values for postgresql
                    lat = coord.text[18:30] #Flipped values for sqlite3
                    c = CoordinateData(latitude=float(lat), longitude=float(lng))
                    c.save()


    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epl.settings')
        django.setup()
        self._create_tags()
