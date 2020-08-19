# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:09:59 2020

@author: Woody
"""

import csv
import json
import time
import glob

#initial read csv and save as a json file


def createFromCSV():

    csvAvailable=glob.glob('./csv/*.csv')
    print("please select a csv to import. Must have two columns with Question/Answer pairs")
        
    for idx, file in enumerate(csvAvailable):
        print(idx+1, end = '')
        print(": ", end = '')
        print(file[6:])  #numberical factors to remove "./Decks\" beginning and end
    
    response=input("")
    while (not(response.isdigit()) or (int(response))>len(csvAvailable) or (int(response))<1):
        response=input("Please type a number between 1 and %d: " % len(csvAvailable))  
    
    
        
    data={}
    data['meta']={}    
    data['deck']={}
    with open(csvAvailable[int(response)-1]) as csvfile:
        csvdata = csv.reader(csvfile)
        for idx, row in enumerate(csvdata):
            data['deck'][idx]={'card': {}, 'history' : {}, 'prerequesites' : {}}
            data['deck'][idx]['card']['type']='multi'
            data['deck'][idx]['card']['question']=row[0]
            data['deck'][idx]['card']['answer']=row[1]
            data['deck'][idx]['history']['created']=int(time.time())
            data['deck'][idx]['history']['nextRecall']=int(time.time())
            data['deck'][idx]['history']['box']=0
            data['deck'][idx]['history']['responses']={}
    
    response=input('Please enter a Title for the deck: ')
    data['meta']['Title']=response
    response=input('Please enter a unique ID for this deck: ')    
    data['meta']['ID']=response
    response=input('Please enter a category for this deck: ')    
    data['meta']['category']=response #we need to come up with a system for categories someday
    response=input('if relevant, Please type the preceding part of each question to be shown. e.g. "What is the captial city of "<question>\n')    
    data['meta']['baseQ']=response  #precedes every question in the list
    response=input('if relevant, Please type the following part of each question to be shown. e.g. <question>" is the capital city of which country?"\n')    
    data['meta']['followQ']=response  #follows every question in the list
    
    with open("Decks/"+data['meta']['ID']+'.json', 'w') as fp:
        json.dump(data, fp)
    
    print("\nDone!\n")
    
    