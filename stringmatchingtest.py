# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:20:13 2020

@author: Woody
"""

import jellyfish

print(jellyfish.levenshtein_distance(u'jellyfish', u'smellyfish'))

print(jellyfish.levenshtein_distance(u'jellyfish', u'smellyfish123123123'))
print(jellyfish.levenshtein_distance(u'123123123', u'smellyfish'))
print(jellyfish.levenshtein_distance(u'smellyfish', u'smellyfish'))

print("**********")
print(jellyfish.jaro_distance(u'jellyfish', u'smellyfish'))

print(jellyfish.jaro_distance(u'jellyfish', u'123123123123'))
print(jellyfish.jaro_distance(u'jellyfish123123123', u'123123123123Jellyfish'))