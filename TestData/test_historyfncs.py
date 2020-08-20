# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:20:12 2020

@author: Woody
"""
import os
import sys
import random
import datetime
sys.path.append(os.path.abspath('../'))
from generatejson import *
from updateQuestionHistory import *


def test_getNextRecallInterval():
    result = getNextRecallInterval(random.randrange(8))
    assert type(result)==datetime.timedelta
    assert result.seconds>-1
    
#test_getNextRecallInterval()

def test_updateBox():
    
    level=random.randrange(8)
    newBox=updateBox(level,8,1)
    assert newBox>level-1
    assert newBox<8
    newBox=updateBox(level,8,0)
    assert newBox>-1
    assert newBox<level+1