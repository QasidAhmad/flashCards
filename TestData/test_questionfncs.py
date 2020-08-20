# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 14:56:50 2020

@author: Woody
"""


import os
import sys
import random

sys.path.append(os.path.abspath('../'))

from displayquestion import askQuestion

def test_askQuestion():
    result=askQuestion() #needs dummy deck
    assert isinstance(result,int)