#using bings maps api
import userLocation
import search

import urllib.request, urllib
import json

bingsMapsKeys = "<Your API KEY here>"

def geoEncode(flag):
    if flag == 1:
        latitude, longitude = userLocation.getLocation()
    else: 
        latitude, longitude = search.searchLocation()

    geoCode = "http://dev.virtualearth.net/REST/v1/Locations/" + latitude + "," + longitude + "?key=" + bingsMapsKeys

    uh = urllib.request.urlopen(geoCode)
    data = uh.read().decode()

    try:
        js = json.loads(data)
        location = js['resourceSets'][0]['resources'][0]['address']['formattedAddress']
        print(location)
        return(latitude, longitude, location)
    except:
        js = None
        if not js or 'statusCode' not in js or js['statusCode'] != 200:
            print('An error occured. Please check the spelling and try again')