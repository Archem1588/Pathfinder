# Database --> KML

from xml.dom.minidom import Document
import sqlite3
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = os.path.join(BASE_DIR,'db.sqlite3')


def getKml():
    # Create XML document, append KML root element
    doc = Document()

    kml = doc.createElement('kml')
    doc.appendChild(kml)

    kml.setAttribute('xmlns', 'http://earth.google.com/kml/2.2')

    document = doc.createElement('Document')
    kml.appendChild(document)

    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM bikeways_coordinatedata')
    rows = c.fetchall()
    for row in rows:
        addCoordinate(doc,
                      document,
                      row[1],
                      row[2])
    c.close()
    conn.close()

    return doc.toprettyxml(indent='  ')


def addCoordinate(doc, document, latitude, longitude):
    coordinate = doc.createElement('Coordinate')
    document.appendChild(coordinate)

    point = doc.createElement('Point')
    coordinate.appendChild(point)

    coordinates = doc.createElement('coordinates')
    point.appendChild(coordinates)
    coordinatesText = str(latitude) + ',' + str(longitude) + ",0"
    coordinates.appendChild(doc.createTextNode(coordinatesText))

print('Content-type: text/xml\n')
print(getKml())
