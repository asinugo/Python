# Example code to read from AccuWeather's API
# Spring 2020
# You need to update the API variable with your API Key from AccuWeather

import json
import time
import urllib.request

API = "PUT YOUR API KEY HERE"
LOCATION_ID = "17824_PC"
apiurl = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (LOCATION_ID, API)
print(apiurl)
with urllib.request.urlopen(apiurl) as url:
    data = json.loads(url.read().decode())
print(data)
