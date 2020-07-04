# Example code to read an AccuWeather's API response from a file to allow us
# to test our parsing logic.
# This works in conjunction with weather_api_save.py
# Spring 2020
import json
# Update the location below for where the file is stored.
f = open("c:/tmp/accu.tmp","r")
data=json.loads(f.read())
f.close()
# Put your test code here.
