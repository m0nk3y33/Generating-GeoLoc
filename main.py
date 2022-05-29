# import pandas as pd
# import time
import csv
from geopy.geocoders import Nominatim


with open("Adresy.csv", newline='') as csvfile:
    rows = csv.reader(csvfile,)
    data = {}

    for row in rows:
        data[row[0]] = row[0:]

    for key in data:

        nazwa = f"{data[key][0]}"
        kod = f"{data[key][1]}"
        adres = f"{data[key][2]},{data[key][3]}"


        adres = adres.upper()
        adres = adres.replace("UL.", "")

        locator = Nominatim(user_agent="myGecoder")
        location = locator.geocode(adres)

        if location != None:
            print(adres, ";", location.latitude,";", location.longitude, ";", kod, ";", nazwa)







