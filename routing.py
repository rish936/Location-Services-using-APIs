import urllib.request, urllib
from PIL import Image
import requests
from io import BytesIO
import json
import userLocation
import search

def direction(dec):
    bingsMapsKeys = "<Your API KEY here>"

    if dec == 1:
        latitude, longitude = userLocation.getLocation()
    if dec == 2:
        latitude, longitude, location = search.searchLocation()

    destlatitude, destlongitude, destlocation = search.searchLocation()
    route = "https://dev.virtualearth.net/REST/v1/Imagery/Map/Road/Routes?wp.0=" + str(latitude) + "," + str(longitude) + ";64;1&wp.1=" + str(destlatitude) + "," + str(destlongitude) + ";66;2&mapSize=2000,1500&key=" + bingsMapsKeys


    im = Image.open(requests.get(route, stream=True).raw)
    im.show()