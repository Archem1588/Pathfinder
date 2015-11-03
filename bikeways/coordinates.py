import sqlite3
import os
import json
import urllib
import psycopg2
from urllib import parse

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = os.path.join(BASE_DIR,'db.sqlite3')


def connectDB():

    #urllib.parse.uses_netloc.append("postgres")
    #url = urllib.parse.urlparse(os.environ["DATABASE_URL"])
    #conn = sqlite3.connect(db)
    conn_string = "host='localhost' dbname='tomato' user='postgres' password='postgres'"
    conn = psycopg2.connect(conn_string)
    #conn_string = "host='ec2-107-21-221-107.compute-1.amazonaws.com' dbname='d9fa7k286sn968' user='dyrznugctzdrhv' password='yOjq_K_ltjglgZ0wNdl8F1nb6U'"
    #conn = psycopg2.connect(conn_string)
    #conn = psycopg2.connect(
    #database=url.path[1:],
    #user=url.username,
    #password=url.password,
    #host=url.hostname,
    #port=url.port
#)
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
        lats.append(row[1])
    lat = lats[0] # just getting the first lat point
    return json.dumps(lat)

def getLngs():
    rows = connectDB()
    lngs = []
    for row in rows:
        lngs.append(row[2])
    lng = lngs[0] # just getting the first lng point
    return json.dumps(lngs)

def getCoords():
    rows = connectDB()
    coordinates = []
    for row in rows:
        coordinates.append({'lat': row[1], 'lng': row[2]})
    return(json.dumps(coordinates))

getCoords()