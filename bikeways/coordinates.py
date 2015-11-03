import sqlite3
import os
import json
import psycopg2
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = os.path.join(BASE_DIR,'db.sqlite3')


def connectDB():
    #conn = sqlite3.connect(db)
    conn_string = "host='localhost' dbname='tomato' user='postgres' password='postgres'"
    conn = psycopg2.connect(conn_string)
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