# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 08:33:50 2021

@author: Jorge
"""

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?";
orig = "Quito"
dest = "Guayaquil"
key = "VwsE2KY3PeLmjS2lpSmwyNrBFkmAAj6I"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data=requests.get(url).json()
print(json_data)
print("URL:"+(url))

json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

if json_status== 0:
    print("API Status: " + str(json_status) + "= A succeful route call.\n")