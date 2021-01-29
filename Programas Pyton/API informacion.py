# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:41:57 2021

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
        print("Kilometers:         " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel(Ltr):          " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("==================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + "(" +str("{:.2f}".format((each["Distance"])*1.61)+ "Km") )
            print("==================================")
        
    elif json_status == 402:
        print("****************")
        print("For status Code: " + str(json_status) + ";Invalid user inputs for one or both locations.")
        print("****************\n")
        print("================================================")
    else:
        print("*********************")
        print("For Status Code: " + str(json_status) + ", Refer to:")
        print("https://developer.papquest.com/documentation/directions-api/status-codes")
        print("**********************\n")
        
        