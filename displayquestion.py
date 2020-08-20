# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 08:57:22 2020

@author: Woody
"""

import random
import time
from generatejson import createFromCSV
  
def deckStats(deck):
    total=[0,0,0,0,0,0,0,0]
    overdue=0
    now=time.time()
    
    for card in deck['deck']:
        if deck['deck'][card]['history']['box']==0:
            total[0]+=1
        for box in range(1,len(total)):
            if deck['deck'][card]['history']['box']==box:
                total[box]+=1
                if deck['deck'][card]['history']['nextRecall']<now:
                    overdue+=1
    
    print("There are " + str(len(deck['deck'])) + " cards in this deck")
    print("You have " + str(total[0]) + " unviewed cards")
    print("You have " + str(overdue) + " overdue cards")
    for i in range(1,len(total)):
        print("Box " + str(i) + " has " + str(total[i]) + " cards")
    
    return overdue, total
            
def askQuestion(deck, number):  #interface after card selector
    print(deck['meta']['baseQ'], end = '')
    print(deck['deck'][number]['card']['question'], end = '')
    print(deck['meta']['followQ'], end = '')
    print(':')
    position = random.randrange(4)
    for i in range(4):
        print(i+1, end = '')
        print(": ", end = '')
        if (i == position):
            print(deck['deck'][number]['card']['answer'])
        else:
            print(getRandomAnswer(deck['deck'], number))
    return(position+1)
    
def getRandomAnswer(deck, initcard):  #pulls a random answer from elsewhere on the card to fill out the multiple choice
    card=random.choice(list(deck.keys()))
    #print(card)
    if (card==initcard):  #only accept answer if its a diferent card
        return getRandomAnswer(deck, initcard)
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
  
import json
import glob

def initialiseSession():
    
    print("Welcome Back! \n Please choose the deck you want to learn today:")
    
    decksAvailable=glob.glob('./Decks/*.json')
    idx=-1
    for idx, file in enumerate(decksAvailable):
        print(idx+1, end = '')
        print(": ", end = '')
        print(file[8:-5])  #numberical factors to remove "./Decks\" beginning and ".json" end
    print(idx+2, end = '')
    print(": ", end = '')
    print("Import new deck from CSV")
    response="0"    
    while (not(response.isdigit()) or (int(response))>(len(decksAvailable)+1) or (int(response))<1):
        response=input("Please type a number between 1 and %d: " % (len(decksAvailable)+1))
    if (int(response)==len(decksAvailable)+1):
        createFromCSV()
        return initialiseSession()
    else:
        filename=decksAvailable[int(response)-1]
        with open(filename, 'r') as fp:
            questions = json.load(fp)
        return questions, filename
    #needs check of json file
        
def numberOfCards(deck):    
    
    print("\n How many cards do you want to look at in this session?")
    totalCards="-1"  
    while (not(totalCards.isdigit()) or (int(totalCards))>(len(deck['deck'])-1) or (int(totalCards))<0):
        totalCards=input("Please type a number between 1 and %d: " % (len(deck['deck'])-1))
        
    totalCards=int(totalCards)
    return totalCards

def enterToContinue():  #gives user chance to have a break or exit
    print('\n\nPress "Enter" to continue (x to exit)')
    checkexit=input("")  #gives a chance to exit early
    if checkexit=="x":
        print('Goodbye...')
        raise SystemExit
    
def giveFeedback(checkA, answer):
    if checkA[0]:
        
        print("\033[37;42mCorrect!\033[m, it took you %.1f seconds" % checkA[1])
    else:
        print("\n\033[37;41mWrong!\033[m")
        print("The Correct Answer was ", end = '')
        print(answer)
        
def showProgress(Quest, totalCards):  #prints progress bar to screen
    length=40
    print("\ncompleted %d questions out of %d" % ((Quest+1), totalCards))
    for j in range(length):
        if (j > ((Quest+1) * length /totalCards)):
            print("_", end = '')  #print a progress bar
        else:
            print("█", end = '')
   
class newSession(Exception): pass
         
def endSession(totalCards):  #will show how well user did and give options to continue
    print("\n you got X correct out of %d cards" % totalCards) 
    
    print("\nWhat shall we do now?")
    print("1: Do some more cards?")
    print("2: New Deck?")
    print("3: Exit")
    
    response=input("")
    while (not(response.isdigit()) or (int(response)>3) or (int(response))<1):
        response=input("Please type a number between 1 and 3: ")
    
    if (response=="3"): 
        raise SystemExit
    elif (response=="2"): 
        raise newSession
    else:    
        
        pass
        # goes back to same while loop automatically
    
def testingDisplay():
    try:
        endSession(10) #need to bypass user input
        print("endSession pass")
    except:
        print ("endSession fail, expected: not to crash")