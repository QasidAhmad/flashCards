# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:18:39 2020

@author: syedq
"""

# testing receiving deck from another module

import sendDeck

deck = sendDeck.returnDeck()

#print(deck)

#print(type(deck))

#print(deck.keys())
#print(deck['1']['history'])

history = deck["deck"]["1"]["history"]

print(history["responses"])

if "responses" in history:
    print("key present")
    
else: print("key missing")