#!/usr/bin/python

# Takes a food name and searches wikipedia for information
# relating to the food. Requires google's api to be installed
# by 'pip install --upgrade google-api-python-client'


import sys
import json
from googleapiclient.discovery import build


def get_food_url(food = "Hamburger"):
    # Get the config file information
    with open('config') as f:
        credentials = f.read().splitlines()
    key = credentials[2]


    # Build the service with personal developer key
    service = build("customsearch", "v1",
                    developerKey=key)


    # Search wikipedia using the tag passed in, and the service built
    res = service.cse().list(
        q=food,
        cx='015475052380168548381:it0vthdy1i8',
        ).execute()
    url = res[u'items'][0][u'link']
    url = url[:]

    # Output the top result's url
    return url
