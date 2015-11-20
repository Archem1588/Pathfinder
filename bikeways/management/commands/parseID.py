__author__ = 'hannahpark'
from django.core.management.base import BaseCommand
from xml.etree.ElementTree import ElementTree
from bikeways.models import CoordinateWithID
import os
import django


class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):

        tree = ElementTree()
        data = tree.parse('bikeways.kml')
        placemark = data.findall('.//{http://www.opengis.net/kml/2.2}Placemark')

        i = 1
        for multiGeom in placemark:
            placemarkid = i
            for item in multiGeom:
                for lineString in item:
                    for coord in lineString:
                        key = placemarkid
                        lng = coord.text[0:12]
                        lat = coord.text[18:30]
                        latString = str(lat)
                        latFirstDigit = latString[0]
                        if latFirstDigit != "4":
                            lat = coord.text[17:29]
                        latString = str(lat)
                        latFirstDigit = latString[0]
                        if latFirstDigit != "4":
                            lat = coord.text[16:28]

                        # print(key)
                        print(lat)
                        # print(lng)
                        c = CoordinateWithID(key=key, latitude=float(lat), longitude=float(lng))
                        c.save()

            i += 1


    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epl.settings')
        django.setup()
        self._create_tags()