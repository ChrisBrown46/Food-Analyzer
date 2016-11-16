#!/usr/bin/python

# Takes a food name and searches wikipedia for information
# relating to the food. Requires google's api to be installed
# by 'pip install --upgrade google-api-python-client'


import pprint
import sys
from googleapiclient.discovery import build


# Get the config file information
with open('config') as f:
    credentials = f.read().splitlines()
key = credentials[2]


# Read input on what food to search for
if len(sys.argv) != 2:
    sys.exit('No input')
food = sys.argv[1]


# Build the service with personal developer key
service = build("customsearch", "v1",
                developerKey=key)


# Search wikipedia using the tag passed in, and the service built
res = service.cse().list(
    q=food,
    cx='015475052380168548381:it0vthdy1i8',
    ).execute()


# Output the results to a file labeled 'Food_Info.txt'
open("Food_Info.txt", "w").close()
with open("Food_Info.txt", "a") as text_file:
    text_file.write(food + "\n\n")
    text_file.write(pprint.pformat(res))
print "Image successfully tagged and stored in 'Food_Info.txt.txt'"

