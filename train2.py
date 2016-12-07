from clarifai.rest import ClarifaiApp
import os, os.path
import numpy as np
from sklearn import svm
import ast
from sklearn.externals import joblib

with open('config') as f:
    credentials = f.read().splitlines()

# Create a food model for Clarifai
app = ClarifaiApp(credentials[0], credentials[1])
model = app.models.get("food-items-v1.0")

clf = svm.SVC(kernel='linear')


def train():
    targetList = []
    tagList = [[]for _ in range(93)]

    # creating the list for the target values. In our case it's the number of food label we have.
    for i in xrange(93):
        targetList.append(i)

    # reading in the images for training
    tagsPath = "Image_Tags"
    labelNum = 0

    # reading the vectorized tags and training the SVM with them.
    # The fits the SVM line by line. We may decide to change this based on the results we get.
    # converting the string we receive and converting them to floats, then storing the numbers for training.
    for item in os.listdir(tagsPath):
        f = open(tagsPath + "/" + item, 'r')
        for line in f:
            values = line.strip('\n[]')
            newString = values.replace(" ", "")
            finalString = newString.replace(",", "")
            for i in xrange(len(finalString)):
                tagList[labelNum].append(float(finalString[i]))

        labelNum += 1

    # for i in xrange(len(tagList)):
    #     print len(tagList[i])

    clf.fit(tagList, targetList)
    # saving the training for later use.
    joblib.dump(clf, 'training.pkl')


#We'll need to change this fucntion so that we use the reform tags method of vectorizing
def test():
    clf2 = joblib.load('test.pkl')

    testList = []

    testOutput = model.predict_by_filename('applePieTest.jpg')
    testOutput = testOutput[u'outputs'][0][u'data'][u'concepts']

    for testFood in testOutput:
        testList.append(testFood['name'])

    # to do - vecortize the image tags

    # print test1.shape
    # prediction = clf2.predict(test1)

    #print prediction




train()