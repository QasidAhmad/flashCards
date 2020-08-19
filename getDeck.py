# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:18:39 2020

@author: syedq
"""

# testing receiving deck from another module

import sendDeck

deck = sendDeck.returnDeck()

print(deck)

print(type(deck))