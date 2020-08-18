# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:01:25 2020

@author: Woody

organises program structure and flow
"""
import random
import json
import glob

from updateQuestionsHistory import updateQuestionsHistory
from displayquestion import *


def main():
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
    
    print("\nYou last accessed this deck X days/weeks ago. There are %d cards in this deck, X are new to you, Y are overdue. (other stats about the deck here). How many do you want to look at in this session?" % (len(questions)-1))
    totalCards="-1"  
    while (not(totalCards.isdigit()) or (int(totalCards))>(len(questions)-1) or (int(totalCards))<0):
        totalCards=input("Please type a number between 1 and %d: " % (len(questions)-1))
        
    totalCards=int(totalCards)
    #return
    
        
    for Quest in range(totalCards):
        
        #get next question to be asked:
        nextQ=str(random.randrange(200))
        ###############################
        
        position=askQuestion(questions,nextQ)
        checkA=checkAnswer(position)
    
        difficulty = askDifficulty()
        
        
    
        if checkA[0]:
            print("Correct!, it took you %.1f seconds" % checkA[1])
        else:
            print("\nWrong!")
            print("The Correct Answer was ", end = '')
            print(questions[nextQ]["card"]["answer"])
            
        #updateQuestionsHistory(deck,number,time.time(),checkA[0],checkA[1],difficulty)
        
        
        
        print("\ncompleted %d questions out of %d" % ((Quest+1), totalCards))
        for j in range(40):
            if (j > ((Quest+1) * 40 /totalCards)):
                print("_", end = '')  #print a progress bar
            else:
                print("█", end = '')
        
        print("\n")
        
        print('Press "Enter" for next card')
        checkexit=input("")  #gives a chance to exit early
        if checkexit=="x":
            print('Goodbye...')
            return

main()