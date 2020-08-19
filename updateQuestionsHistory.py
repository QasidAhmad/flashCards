import json
import datetime 
from datetime import timedelta
import sendDeck

def updateBox(currentBox,maxBoxes,correctness, method="default"):
    if method == "default":
        if currentBox > maxBoxes:
            print("Error: current box cant be greater than max boxes")
        else:
            if correctness == 1:
                if currentBox == maxBoxes:
                    updatedBox = currentBox
                    print("Reached the last box, congrats")
                if currentBox < maxBoxes:
                    updatedBox = currentBox + 1
            
            elif correctness == 0:
                currentBox = 0
    else: 
        print("Error: Unknown box updating method")
        
    return updatedBox


def getNextRecallInterval (box):
    boxIntervals = [timedelta(seconds=5),
                    timedelta(seconds=25),
                    timedelta(minutes=2),
                    timedelta(minutes=10),
                    timedelta(hours=1),
                    timedelta(hours=5),
                    timedelta(days=5)]
    
    return  boxIntervals[box]
    
    

def updateQuestionHistory(deck,questionID, correctness,thinkingPeriod,difficulty):
    

	#correctness: 0 incorrect, 1 corect
	#difficulty, value 0-9 0 is too easy 9 is too hard (integer for now but could be float later
	
	# Takes new question response data (timestamp,correctness,thinkingPeriod,difficulty)
	# and updates question history 

	
    # get section of Deck (questions history) to update
    questionHistory = deck['deck'][str(questionID)]['history']
    
    
    #update box number
    maxBoxes = 8 # todo: refactor to avoid this magic number
    questionHistory["box"] = updateBox(questionHistory["box"],maxBoxes,correctness)
  	
    #update next recall time
    nextRecallInterval = getNextRecallInterval(questionHistory["box"])	
    nextRecall = datetime.datetime.now() + nextRecallInterval
    nextRecallSinceEpoc = nextRecall- datetime.datetime(1970,1,1)
    nextRecallSecsSinceEpoc= round(nextRecallSinceEpoc.total_seconds())
    deck['deck'][str(questionID)]['history']['nextRecall'] = nextRecallSecsSinceEpoc

	#create new response entry
    newResponse = {"correctness":correctness,
                   "datestamp":datetime.datetime.now(),
                   "thinkingPeriod":thinkingPeriod,
                   "difficulty":difficulty}
    
    
    #update new response to history
        #get respone index
    responseIndex = len(questionHistory["responses"])
    
        #update response at index position
    deck['deck'][str(questionID)]['history']['responses'].update(
                {str(responseIndex):newResponse})
    
    #checking it all looks good               
    #deck['deck'][str(questionID)]['history']['responses']
    


#testing function
caps_deck=sendDeck.returnDeck()#get deck 

updateQuestionHistory(deck=caps_deck,questionID=1,correctness=1,thinkingPeriod=1,difficulty=1)


print(caps_deck["deck"]["1"]["history"]["nextRecall"])

if  (caps_deck["deck"]["1"]["history"]["responses"]["0"]["correctness"]==1 and
    caps_deck["deck"]["1"]["history"]["box"]==1) :
    print("Test passed")

else: print("Test failed")