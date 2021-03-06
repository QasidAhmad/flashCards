# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:01:25 2020

@author: Woody

organises program structure and flow
"""

from selectNextCard import selectNextCard

from updateQuestionHistory import updateQuestionHistory,getNextRecallInterval,updateBox
from displayquestion import *


def main():
    
    
    deck, file = initialiseSession()
    
    try:
        while True:
            totalCards = numberOfCards(deck['deck'])
            #above is select session
            
                
            for Quest in range(totalCards):
                
                enterToContinue()  #gives user chance to have a break or exit
                
                #get next question to be asked:
                nextQ=selectNextCard(deck,"newlast")   #select card #todo replace argument (0) with history
                ###############################
                
                position=askQuestion(deck,nextQ) #prsents card to user and returns the postition of the correct answer (1-4)
                
                checkA=checkAnswer(position)     #checks whether answer response is correct and time to answer
            
                difficulty = askDifficulty()     #difficulty response
                      
                giveFeedback(checkA,deck['deck'][nextQ]["card"]["answer"])  #gives feedback to the user
                print(checkA)
                updateQuestionHistory(deck=deck,file=file,questionID=nextQ,correctness=checkA[0],thinkingPeriod=checkA[1],difficulty=difficulty)
                
                showProgress(Quest, totalCards) #simple progress bar
                
            #end session presented here, what to display, what options should be given?
            endSession(totalCards)  
    except newSession:
        main()
            
main()