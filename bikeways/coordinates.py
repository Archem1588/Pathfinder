import sqlite3
import os
import json
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db = os.path.join(BASE_DIR,'db.sqlite3')


def getPoint():
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('SELECT * FROM bikeways_coordinatedata')
    rows = c.fetchall()
    for row in rows:
        print(row[1]) # latitudes from database
    c.close()
    conn.close()

getPoint()