# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:21:55 2021

@author: Jorge
"""

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?";
while True:
    orig=input("Localizacion de inicio: ")
    dest=input("Destino: ")
    key = "VwsE2KY3PeLmjS2lpSmwyNrBFkmAAj6I"
    url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
    print("URl: "+ (url))
   
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]

    if json_status== 0:
        print("API Status: " + str(json_status) + "= A succeful route call.\n")