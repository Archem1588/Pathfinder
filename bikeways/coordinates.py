import sqlite3
import os
import json
import psycopg2
#import urllib.parse
#from urllib.parse import urlparse, uses_netloc
import urlparse


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = os.path.join(BASE_DIR,'db.sqlite3')


def connectDB():

    # <-----postgresql----->
    #conn_string = "host='localhost' dbname='tomato' user='postgres' password='postgres'"
    #conn = psycopg2.connect(conn_string)

    # <----sqlite3---->
    #conn = sqlite3.connect(db)

    # <----Python 3.x Heroku ----->
    # urllib.parse.uses_netloc.append("postgres")
    # url = urllib.parse.urlparse(os.environ["DATABASE_URL"])

     # <----Python 2.7 Heroku ---->
    urlparse.uses_netloc.append("postgres")
    url = urlparse.urlparse(os.environ["DATABASE_URL"])

    conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
    )

    c = conn.cursor()
    c.execute('SELECT * FROM bikeways_coordinatedata')
    rows = c.fetchall()
    c.close()
    conn.close()
    return rows

def getLats():
    rows = connectDB()
    lats = []
    for row in rows:
        lats.append(row[2])
    return json.dumps(lats)

def getLngs():
    rows = connectDB()
    lngs = []
    for row in rows:
        lngs.append(row[1])
    return json.dumps(lngs)

def getCoords():
    rows = connectDB()
    coordinates = []
    for row in rows:
        coordinates.append({'lat': row[1], 'lng': row[2]}) #Bug here!
        # sqlite3: lat: row[2], lng: row[1]
        # postgresql: lat: row[1], lng: row[2]
    return json.dumps(coordinates)

getCoords()