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
    #for row in csvdata:
        #cardArray.append(row)
    for idx, row in enumerate(csvdata):
        cardArray.append(row)
        data[idx]={'card': {}, 'history' : {}}
        data[idx]['card']['type']='multi'
        data[idx]['card']['question']=row[0]
        data[idx]['card']['answer']=row[1]
        data[idx]['history']['created']=int(time.time())
        
        #print(row)
       # data[]
        #print(', '.join(row))
    
print(cardArray[6][1])
print(cardArray[7])



#data[1]['card']['type']='multi'
#data[1]['card']['question']='test'
#data[1]['card']['answers']={1:'hi', 2:'testing', 3:1, 4:'boo!'}
#data[1]['card']['answer']=3


#data[1]['history']['created']=int(time.time())


    
	#data[rowindex]={'card': {"Question"=row[0],"Answer"=row[1]}, 'history' : {}}


print(len(data[1]['card']))

with open('data.json', 'w') as fp:
    json.dump(data, fp)
    
with open('data.json', 'r') as fp:
    data2 = json.load(fp)
    
    
print(data2)