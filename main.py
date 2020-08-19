# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 16:01:25 2020

@author: Woody

organises program structure and flow
"""
import random


from updateQuestionsHistory import updateQuestionHistory
from displayquestion import *


def main():
    
    
    totalCards, questions = initialiseSession()
    #above is select session
    
        
    for Quest in range(totalCards):
        
        enterToContinue()
        
        #get next question to be asked:
        nextQ=str(random.randrange(200))   #select card
        ###############################
        
        position=askQuestion(questions,nextQ) #present card position is the position of the correct answer out of 4
        
        checkA=checkAnswer(position)     #checks answer response and time to answer
    
        difficulty = askDifficulty()     #difficulty response
              
        giveFeedback(checkA,questions[nextQ]["card"]["answer"])
            
        #updateQuestionsHistory(deck,number,time.time(),checkA[0],checkA[1],difficulty)
        
        showProgress(Quest, totalCards)
        
    #end session presented here, what to display, what options should be given?
    endSession(totalCards)  
        
            

main()