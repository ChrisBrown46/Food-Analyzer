#!/usr/bin/python

import sys
import os
import fnmatch
import json
from clarifai import rest
from clarifai.rest import ClarifaiApp


# GENERATE_TAGS_FOR_IMAGE Returns a list of tags taken from Clarifai
# that represent the food items found in a picture.
# Ex) tags = generate_tags_for_image('/tmp/user/dog.jpg', 0)
# Then second argument is 0 for a local file, 1 for a url

def generate_tags_for_image(image, method):
    
    # Get the config file information
    with open('config') as f:
        credentials = f.read().splitlines()
        

    # Create a food model for Clarifai
    app = ClarifaiApp(credentials[0], credentials[1])
    model = app.models.get("food-items-v1.0")


    # Capture the tags for the picture in a list
    if method == "url":
        output = model.predict_by_url(url = image)
    else:
        output = model.predict_by_filename(filename = image)
    output = output[u'outputs'][0][u'data'][u'concepts']


    # Return the tags as a list
    tags = []
    counter = 0
    if output != None:
        for tag in output:
            if counter <= 9:
                tags.append(str(tag[u'name']))
                counter += 1
    return tags
