import os
import sys
from datetime import datetime
import sqlite3 as lite

file = open("locations.json","w")
con = lite.connect('db/pos.db')
cur = con.cursor()

def begin():
    file.write('markers = [')

def end():
    file.write('];')

def writecoord(lat, long, time):
    file.write('\n   {\n         "name": "')
    file.write(time+'",\n         "url": "",\n         "lat": ')
    file.write(lat+',\n         "lng": ')
    file.write(long+'\n   },')

def getdatab():
    # choose = 0
    with con:
        cur.execute("SELECT lat, long, time FROM pos")
        rows = cur.fetchall()
        for row in rows:
            # if(choose % 2 == 0):
            if(row[0]=="0.0" or row[1]=="0.0" or row[0]=="nan" or row[1]=="nan"):
                print("no gps signal")
            else:
                print(row)
                writecoord(row[0],row[1],row[2])
                # choose += 1


if __name__ == '__main__':
    begin()
    getdatab()
    end()

file.close()
