import sqlite3
import time

import requests
from bs4 import BeautifulSoup
import datetime

def temperature_record():
    response = requests.get("https://www.yr.no/en/forecast/hourly-table/2-456172/Latvia/R%C4%ABga/R%C4%ABga/Riga?i=1")
    soup = BeautifulSoup(response.content, 'html.parser')

    temp = soup.find(class_='temperature temperature--warm-primary').text
    temp = temp.replace("Temperature", "")
    temp = temp.replace("°", "")
    print(temp)

    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    connection = sqlite3.connect("weather.sl3", timeout=5)
    cur = connection.cursor()
    cur.execute(f"INSERT INTO weather (date, temperature) VALUES ('{date}', '{temp}');")
    connection.commit()
    connection.close()

connection = sqlite3.connect("weather.sl3", timeout=5)
cur = connection.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS weather (date TEXT,temperature REAL);")
connection.commit()
connection.close()

temperature_record()
while True:
    time.sleep(30*60)
    temperature_record()
