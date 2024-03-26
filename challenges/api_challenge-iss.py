#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    lon=resp["iss_position"]["longitude"]
    lat=resp["iss_position"]["latitude"]

    locator=rg.search((lat, lon))
    city=locator[0]["name"]
    country=locator[0]["cc"]



    time = resp["timestamp"]
    time = datetime.datetime.fromtimestamp(time)


    print(f"""
    Timestamp: {time}
    CURRENT LOCATION OF THE ISS:
    lon: {lon}
    lat: {lat}
    City/Country: {city}, {country}
    """)

if __name__ == "__main__":
    main()
