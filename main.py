# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:01:25 2020

@author: Woody

organises program structure and flow
"""
import random
import selectNextCard

#from updateQuestionsHistory import updateQuestionHistory
from displayquestion import *


def main():
    
    
    questions = initialiseSession()
    
    try:
        while True:
            totalCards = numberOfCards(questions)
            #above is select session
            
                
            for Quest in range(totalCards):
                
                enterToContinue()  #gives user chance to have a break or exit
                
                #get next question to be asked:
                nextQ=str(selectNextCard.selectNextCard(0))   #select card #todo replace argument (0) with history
                ###############################
                
                position=askQuestion(questions,nextQ) #prsents card to user and returns the postition of the correct answer (1-4)
                
                checkA=checkAnswer(position)     #checks whether answer response is correct and time to answer
            
                difficulty = askDifficulty()     #difficulty response
                      
                giveFeedback(checkA,questions[nextQ]["card"]["answer"])  #gives feedback to the user
                    
                #updateQuestionsHistory(deck,number,time.time(),checkA[0],checkA[1],difficulty)
                
                showProgress(Quest, totalCards) #simple progress bar
                
            #end session presented here, what to display, what options should be given?
            endSession(totalCards)  
    except newSession:
        main()
            
main()