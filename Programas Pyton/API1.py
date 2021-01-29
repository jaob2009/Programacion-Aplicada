# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 07:34:34 2021

@author: Jorge
"""



import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?";
orig = "Quito"
dest = "Guayaquil"
key = "VwsE2KY3PeLmjS2lpSmwyNrBFkmAAj6I"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
print("URl: "+ (url))
json_data=requests.get(url).json()
print(json_data)