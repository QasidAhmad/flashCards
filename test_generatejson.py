# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:48:52 2020

@author: syedq
"""
import json
#import generatejson
#from unittest.mock import Mock 
#
#def test_createJSON(self):
#    #testFile = "TestData/jsonCreationTest.json"
#    testDict = {"testKey": "testVal"}
#    file = Mock()
#    createJSON(file,testDict)

def createJSON(file,dict):
    with open(file, 'w') as fp:
        json.dump(dict, fp)

def test_createJSON():
    testFile = "TestData/jsonCreationTest.json"
    testDict = {"testKey":"testVal"}
    createJSON(testFile,testDict)
    
    dictFromJson = json.loads(testFile)
    
    assert dictFromJson["testKey"] == "testVal"

