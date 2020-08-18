# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 08:57:22 2020

@author: Woody
"""

import random
import time
    
def askQuestion(deck, number):  #interface after card selector
    print(deck['deck']['baseQ'], end = '')
    print(deck[number]['card']['question'], end = '')
    print(':')
    position = random.randrange(4)
    for i in range(4):
        print(i+1, end = '')
        print(": ", end = '')
        if (i == position):
            print(deck[number]['card']['answer'])
        else:
            print(getRandomAnswer(deck, number))
    return(position+1)
    
def getRandomAnswer(deck, number):  #pulls a random answer from elsewhere on the card to fill out the multiple choice
    card=random.choice(list(deck.keys()))
    #print(card)
    if ((card==number) or not(card.isdigit())):  #only accept answer if its a diferent, valid, card
        return getRandomAnswer(deck, number)
    else:
        return deck[card]['card']['answer']
        
def checkAnswer(answer):
    startT=time.time()
    response=input("")
    while (not(response.isdigit()) or (int(response))>4 or (int(response))<1):
        response=input("Please type a valid answer number: ")
    questionT=time.time()-startT
    if int(response)==answer:
        return 1, questionT
    else: 
        return 0, questionT
    

def askDifficulty():
    
    response=input("How hard was that?\n0: Too easy, 3: Knew it, 7: Wasn't sure, 9: Complete guess ... ")
    while (not(response.isdigit()) or (int(response))>9 or (int(response))<0):
        response=input("Please type a number 0-9:")
    
    response=int(response)
    if (response<0): response=0
    if (response>9): response=9
    return response
    


    
