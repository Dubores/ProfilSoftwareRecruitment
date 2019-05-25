import sqlite3
import csv
import json
import urllib3
import codecs
import requests
from contextlib import closing
from api import get_csv_url_from_api


db = sqlite3.connect('data/maturadb')
cursor = db.cursor()
url = get_csv_url_from_api()


def insert_data_into_db():
    #checking if table is already created, so that we do not INSERT the same row two times
    #alternative method is creating UNIQUE constraints
    cursor.execute("SELECT count(*) FROM sqlite_master WHERE type ='table' AND name = 'matura'")
    table_count = cursor.fetchall()

    if table_count[0][0] == 0:
        cursor.execute("CREATE TABLE IF NOT EXISTS matura (province TEXT, type TEXT, sex TEXT, year TEXT, no_people TEXT)")
        with closing(requests.get(url, stream=True)) as response:
            csv_reader = csv.reader(codecs.iterdecode(response.iter_lines(), 'WINDOWS-1250'), delimiter=';')
            next(csv_reader)
            for row in csv_reader:
                cursor.execute("INSERT INTO matura (province, type, sex, year, no_people) VALUES(?,?,?,?,?)", (row[0], row[1], row[2], row[3], row[4]))
            db.commit()

def get_data_from_db():
    cursor.execute("SELECT * FROM matura")
    data = cursor.fetchall()
    return data
