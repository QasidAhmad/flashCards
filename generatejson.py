# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 18:09:59 2020

@author: Woody
"""

import csv
import json
import time

#initial read csv and save as a json file

data={}


data['pack']={}
data['pack']['baseQ']="What is the Capital of "  #precedes every question in the list
data['pack']['category']='Geography' #we need to come up with a system for categories

cardArray=[]
with open('Capitals.csv') as csvfile:
    
    csvdata = csv.reader(csvfile)

    for idx, row in enumerate(csvdata):
        #cardArray.append(row)
        data[idx]={'card': {}, 'history' : {}}
        data[idx]['card']['type']='multi'
        data[idx]['card']['question']=row[0]
        data[idx]['card']['answer']=row[1]
        data[idx]['history']['created']=int(time.time())
        

with open('data.json', 'w') as fp:
    json.dump(data, fp)
    
with open('data.json', 'r') as fp:
    data2 = json.load(fp)
    
    