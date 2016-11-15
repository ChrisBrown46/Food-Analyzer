#!/usr/bin/python

# Requires a file called 'config' in the same directory as this file.
# The config file should contain two lines seperated by a newline.
# The first line is the clientId, and the second is the clientSecret.

import sys
import json
from clarifai import rest
from clarifai.rest import ClarifaiApp


# Get the config file information
with open('config') as f:
    credentials = f.read().splitlines()
    

# Create a food model for Clarifai
app = ClarifaiApp(credentials[0], credentials[1])
model = app.models.get("food-items-v1.0")


# Capture the tags for the picture in an array
open("tags.txt", "w").close()
image_url = 'http://dolcecarini.com/wp-content/uploads/2014/07/Cheeseburger.jpg'
if len(sys.argv) == 2:
    image_url = sys.argv[1]
output = model.predict_by_url(url=image_url)
output = output[u'outputs'][0][u'data'][u'concepts']


# Write the tags to the file 'tags.txt'
with open("tags.txt", "a") as text_file:
    text_file.write(image_url + "\n\n")
    for tag in output:
        text_file.write(str(tag[u'name']) + " - " + str(tag[u'value']) + "\n")
print "Image successfully tagged and stored in 'tags.txt'"
