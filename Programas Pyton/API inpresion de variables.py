# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:13:11 2021

@author: Jorge
"""

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?";

while True:
    orig=input("localizacion de inicio: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destino: ")
    if dest == "quit" or dest == "q":
        break
    key = "VwsE2KY3PeLmjS2lpSmwyNrBFkmAAj6I"
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URl: "+ (url))
   
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        print("API Status: " + str(json_status) + "= A succeful route call.\n")
        print("Directions from:    " + (orig)+"to "+ (dest))
        print("Trip Duration:      " + str(json_data["route"]["formattedTime"]))
        print("Miles:              " + str(json_data["route"]["distance"]))
        print("Fuel(Gal):          " +str(json_data["route"]["fuelUsed"]))
        print("==================================")