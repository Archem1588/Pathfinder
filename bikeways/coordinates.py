import sqlite3
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = os.path.join(BASE_DIR,'db.sqlite3')


def connectDB():
    conn = sqlite3.connect(db)
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
    lat = lats[0]
    print(lat)
    return json.dumps(lat)

def getLngs():
    rows = connectDB()
    lngs = []
    for row in rows:
        lngs.append(row[2])
    lng = lngs[0]
    print(lng)
    return json.dumps(lngs)