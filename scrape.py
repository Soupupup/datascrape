# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Import
import pyodbc
import pymssql
import requests
import json
from datetime import datetime

def connect():
    conn = pymssql.connect(server='192.168.104.120',
                          user='bitcoin',
                          password='password',
                           database='bitcoin')
    return conn

# Get the connection
conn = connect()

# Getting a cursor from the connection.
cursor = conn.cursor()

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
r = requests.get(url)
data = json.loads(r.text)
print(data.keys())
currency = data['bpi']
print(data['time'])

date = data['time']['updated']
date =date.replace(' UTC',"")
datetime = datetime.strptime(date, '%b %d, %Y %H:%M:%S')

for key,value in currency.items():
    query = '''insert into dbo.bitcoin values (?,?,?)'''
    cursor.execute(query, date, key, float(value['rate'].replace(",", "")))
    
# Commit and close
cursor.commit()
conn.close()