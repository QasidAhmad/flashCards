# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:20:26 2020

@author: syedq
"""

#testing loading deck and sending it to another function

import json

with open("Decks/capitals-Q.json") as deck_json:
    deck_dict = json.load(deck_json)
    #print(deck_dict) # read success 
    
#print(type(deck_dict)) # dict (test passed)
    
    
def returnDeck():
    return deck_dict


    