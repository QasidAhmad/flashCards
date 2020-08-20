# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:48:52 2020

@author: syedq
"""
import json
import generatejson
#from unittest.mock import Mock 
#
#def test_createJSON(self):
#    #testFile = "TestData/jsonCreationTest.json"
#    testDict = {"testKey": "testVal"}
#    file = Mock()
#    createJSON(file,testDict)



def test_createJSON():
    
    testFile = "TestData/jsonCreationTest.json"
    testDict = {"testKey":"testVal"}
    generatejson.createJSON(testFile,testDict)
    
    #TODO: test json file is actually created with dict in it
    
    
    #dictFromJson = json.loads(testFile)
    
    # assumes previous file does not exist
    #assert dictFromJson["testKey"] == "testVal"
    #print (dictFromJson)

test_createJSON()

