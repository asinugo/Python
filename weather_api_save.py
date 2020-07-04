# Example code to read from AccuWeather's API and save the result to a file
# This allows us to read from the file with another program to test out are
# parsing logic.
# This works in conjunction with weather_api_read_for_testing.py
# Spring 2020

# You need to update the API variable with your API Key from AccuWeather

import json
import time
import urllib.request

# Update with your API Key
API = "PUT YOUR API KEY HERE"
# You can change the location
LOCATION_ID = "17824_PC"
# Update the URL for the query you want. See the API reference at https://developer.accuweather.com/apis
apiurl = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (LOCATION_ID, API)
print(apiurl)
with urllib.request.urlopen(apiurl) as url:
    data = json.loads(url.read().decode())
# This writes the json to a file for later use in testing.
# Update the file location as needed for your system.
f = open("c:/tmp/accu.tmp","w")
f.write(json.dumps(data))
f.close()
