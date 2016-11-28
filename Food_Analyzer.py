#!/usr/bin/python

# Requires a file called 'config' in the same directory as this file.
# The first line is the clientId, and the second is the clientSecret.

import sys
import json
from clarifai import rest
from clarifai.rest import ClarifaiApp


# GENERATE_TAGS_FOR_IMAGE Returns a list of tags taken from Clarifai
# that represent the food items found in a picture. The input is a
# local file path of an image.
# Ex) tags = generate_tags_for_image('/tmp/user/dog.jpg')
def generate_tags_for_image(image_file):
    
    # Get the config file information
    with open('config') as f:
        credentials = f.read().splitlines()
        

    # Create a food model for Clarifai
    app = ClarifaiApp(credentials[0], credentials[1])
    model = app.models.get("food-items-v1.0")


    # Capture the tags for the picture in a list
    output = model.predict_by_filename(filename = image_file)
    output = output[u'outputs'][0][u'data'][u'concepts']


    # Return the tags as a list
    tags = []
    for tag in output:
        tags.append(str(tag[u'name']))
    return tags
