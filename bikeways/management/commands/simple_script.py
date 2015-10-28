from django.core.management.base import BaseCommand
from xml.etree.ElementTree import ElementTree
from bikeways.models import CoordinateData
import os
import django



class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_tags(self):

        # c = CoordinateData(latitude=0.00, longitude=3.14)
        # c.save()
        tree = ElementTree()
        data = tree.parse('bikeways.kml')
        multiGeom = data.findall('.//{http://www.opengis.net/kml/2.2}MultiGeometry')

        # For testing purposes
        lats = []
        lngs = []
        for item in multiGeom:
            for lineString in item:
                for coord in lineString:
                    # lats.append(coord.text[0:12])
                    # lngs.append(coord.text[18:30])
                    lat = coord.text[0:12]
                    lng = coord.text[18:30]
                    c = CoordinateData(latitude=float(lat), longitude=float(lng))
                    c.save()


        # print(len(lats))
        # print(len(lngs))
        # lat = float(lats[0])
        # lng = float(lngs[0])


        # To test for first 4 coordinates
        # i = 0
        # for i in range(0, 4):
        #     print(float(lat[i]))
        #     i += 1

        # coord = data.findall('.//{http://www.opengis.net/kml/2.2}coordinates')
        # for i in coord:
        #     newList = i.text.split()
            # for item in newList:
            #     lat = item[0:12]
            #     lng = item[18:30]
            #     print(float(lat))
            #     print(float(lng))


        # item = newList[0]
        # print(item)
        #for item in newList:
        # lat = item[0:12]
        # lng = item[18:30]
        # c = CoordinateData(latitude=float(lat), longitude=float(lng))
        # c.save()
        # # For testing purposes
        # print(float(lat))
        # print(float(lng))


    def handle(self, *args, **options):
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'epl.settings')
        django.setup()
        self._create_tags()
