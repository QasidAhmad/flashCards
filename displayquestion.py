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
  
import json
import glob

def initialiseSession():
    
    print("Welcome Back! \n Please choose the deck you want to learn today:")
    
    decksAvailable=glob.glob('./Decks/*.json')
    
    for idx, file in enumerate(decksAvailable):
        print(idx+1, end = '')
        print(": ", end = '')
        print(file[8:-5])  #numberical factors to remove "./Decks\" beginning and ".json" end
    response="0"    
    while (not(response.isdigit()) or (int(response))>len(decksAvailable) or (int(response))<1):
        response=input("Please type a number between 1 and %d: " % len(decksAvailable))
    with open(decksAvailable[int(response)-1], 'r') as fp:
        questions = json.load(fp)
    return questions
        
def numberOfCards(questions):    
    print("\nYou last accessed this deck X days/weeks ago. There are %d cards in this deck, X are new to you, Y are overdue. (other stats about the deck here). How many do you want to look at in this session?" % (len(questions)-1))
    totalCards="-1"  
    while (not(totalCards.isdigit()) or (int(totalCards))>(len(questions)-1) or (int(totalCards))<0):
        totalCards=input("Please type a number between 1 and %d: " % (len(questions)-1))
        
    totalCards=int(totalCards)
    return totalCards

def enterToContinue():  #gives user chance to have a break or exit
    print('\nPress "Enter" to continue')
    checkexit=input("")  #gives a chance to exit early
    if checkexit=="x":
        print('Goodbye...')
        return
    
def giveFeedback(checkA, answer):
    if checkA[0]:
        print("Correct!, it took you %.1f seconds" % checkA[1])
    else:
        print("\nWrong!")
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
    
