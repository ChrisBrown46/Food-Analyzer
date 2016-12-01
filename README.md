# Food-Analyzer
Project for CS 5600

To properly run the webpage, please see the next paragraph on how to setup the wikipedia page finder. The webpage is not hosted online, so you will be required to either upload it yourself, or run it on localhost.

To properly use the wikipedia page finder, you will be required to have google's python api client installed. This can be done with 'pip install --upgrade google-api-python-client'. In addition, you will need a developer key from google which can be created by going to https://console.developers.google.com/ then creating an api key for 'customsearch'. After getting a key, put it in as the third line in the config file.

To create your own testing data set for use, you will want to run 'Food_Analyzer.py'. This file contains methods needed to create data for the SVC to learn from. 
To run this program, you must have Clarifai installed along with Python. To install Clarifai through pip, you can use 'pip install clarifai'. 
Also, you are required to have a Clarifai account to process images. Simply replace the stubs in the config file with your own information. 
You will also need to have a folder called 'Images' in the same directory as the file, with sub-folders in 'Images' with the food names. An example set-up can been seen on this github page. In addition, we provided the finished files needed to train the SVC, which can be used as references to help you build your own.
