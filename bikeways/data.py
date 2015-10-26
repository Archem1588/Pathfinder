__author__ = 'hannahpark'
from xml.etree.ElementTree import ElementTree
from .models import CoordinateData

tree = ElementTree()
tree.parse('bikeways.kml')
coord = tree.findall('.//{http://www.opengis.net/kml/2.2}coordinates')
for i in coord:
    newList = i.text.split()
    for item in newList:
        lat = item[0:12]
        lng = item[18:30]
        c = CoordinateData(float(lat), float(lng))
        c.save()
        # For testing purposes
        print(float(lat))
        print(float(lng))

#for i in cleanData:
    # c = CoordinateData.create(i)
    # c.save()
    #coordinate = i.get('coordinates')
    #print(i)

# for attributes in lineStrings:
#     for subAttribute in attributes:
#         if subAttribute.tag == '{http://www.opengis.net/kml/2.2}coordinates':
#             coordinate = subAttribute.get('coordinates')
#             print(coordinate)
#             # c = CoordinateData.create(coordinate)
#             # c.save()


# def extract_coordinates(placemark):
#     if not isinstance(placemark, ElementTree.Element):
#         raise TypeError("given place not of type 'xml.etree.elementTree.Element")
#
#     coordinates = placemark.text.strip()
#     if -1 == coordinates.fine('\n'):
#         return [[float(x) for x in coordinates.split(',')]]
#     else:
#         data = []
#         for triple in coordinates.split('\n'):
#             data.append([float(x) for x in triple.strip().split(',')])
#             return data
#         return None

