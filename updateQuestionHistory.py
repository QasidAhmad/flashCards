#import json
#import datetime 
import time
from datetime import timedelta
#import sendDeck
from generatejson import createJSON

def updateBox(currentBox,maxBoxes,correctness,difficulty, method="default"):
    if method == "default":
        if currentBox > maxBoxes-1:
            currentBox = maxBoxes-1
        else:
            if correctness == 1:
                    
                if currentBox < maxBoxes:
                    updatedBox = currentBox + 1
                if currentBox > maxBoxes-1:
                    updatedBox = maxBoxes
                    print("Reached the last box, congrats!")
            
            elif correctness == 0:
                updatedBox = 0
                
    elif method == "incDifficulty":
        
        difficultyCorrection=int(max(3-difficulty/2,-1)) #move to higher box if too easy or don't move if complete guess
        if currentBox > maxBoxes-1:
            currentBox = maxBoxes-1
        if correctness == 1:
                
            if currentBox < maxBoxes:
                updatedBox = currentBox + 1 + difficultyCorrection
            if updatedBox > maxBoxes-1:
                updatedBox = maxBoxes-1
                print("Reached the last box, congrats!")
        
        elif correctness == 0:
            updatedBox = 1
    else: 
        print("Error: Unknown box updating method")
        updatedBox=0
    return updatedBox


def getNextRecallInterval (box):
    boxIntervals = [timedelta(seconds=0),
                    timedelta(seconds=25),
                    timedelta(minutes=2),
                    timedelta(minutes=10),
                    timedelta(hours=1),
                    timedelta(hours=5),
                    timedelta(days=5),
                    timedelta(days=100)]
    
    return  boxIntervals[box].total_seconds()
  

def updateQuestionHistory(deck,file,questionID, correctness,thinkingPeriod,difficulty):
    

	#correctness: 0 incorrect, 1 corect
	#difficulty, value 0-9 0 is too easy 9 is too hard (integer for now but could be float later
	
	# Takes new question response data (timestamp,correctness,thinkingPeriod,difficulty)
	# and updates question history 

	
    # get section of Deck (questions history) to update
    questionHistory = deck['deck'][str(questionID)]['history']
    
    
    #update box number
    maxBoxes = 8 # todo: refactor to avoid this magic number
    questionHistory["box"] = updateBox(questionHistory["box"],maxBoxes,correctness,difficulty,"incDifficulty")
    print(questionHistory["box"])	
    #update next recall time replace with time.time() version to account for off by 1h error

    nextRecall=int(time.time()+getNextRecallInterval(questionHistory["box"]))
    
    deck['deck'][str(questionID)]['history']['nextRecall'] = nextRecall

	#create new response entry
    newResponse = {"correctness":correctness,
                   "datestamp":int(time.time()),
                   "thinkingPeriod":thinkingPeriod,
                   "difficulty":difficulty}
    
    
    #update new response to history
        #get respone index
    responseIndex = len(questionHistory["responses"])
    
        #update response at index position
    deck['deck'][str(questionID)]['history']['responses'].update(
                {str(responseIndex):newResponse})
    
    createJSON(file,deck)
    
    #checking it all looks good               
    #deck['deck'][str(questionID)]['history']['responses']
    


#testing function
#caps_deck=sendDeck.returnDeck()#get deck 

#updateQuestionHistory(deck=caps_deck,"file",questionID=1,correctness=1,thinkingPeriod=1,difficulty=1)


#print(caps_deck["deck"]["1"]["history"]["nextRecall"])
#
#if  (caps_deck["deck"]["1"]["history"]["responses"]["0"]["correctness"]==1 and
#    caps_deck["deck"]["1"]["history"]["box"]==1) :
#    print("Test passed")
#
#else: print("Test failed")