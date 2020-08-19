import json
import datetime 
from datetime import timedelta
import sendDeck

def updateQuestionHistory(deck,questionID, correctness,thinkingPeriod,difficulty):
    

	#correctness: 0 incorrect, 1 corect
	#difficulty, value 0-9 0 is too easy 9 is too hard (integer for now but could be float later
	
	# Takes new question response data (timestamp,correctness,thinkingPeriod,difficulty)
	# and updates question history 

	
    # get section of Deck (questions history) to update
    questionHistory = deck[str(questionID)]['history']
    
    #update box number
	#updateBox(questionHistory,correctness)

	#update next recall time
	#updateNextRecall(questionHistory,box)

	#increment number of responses
    questionHistory["NumOfResponses"] = questionHistory["NumOfResponses"] +1

	#create new response entry
    newResponse = {"correctness":correctness,
                   "datestamp":datetime.datetime.now(),
                   "thinkingPeriod":thinkingPeriod,
                   "difficulty":difficulty}
    
    
    
    #append new response to history
    questionHistory["Responses"].update(
            {questionHistory["NumOfResponses"]:newResponse})
                     
    print(questionHistory["Responses"][1]["correctness"])
    


#testing function
caps_deck=sendDeck.returnDeck()#get deck 
#print(caps_deck)#ok

test = {"NumOfResponses": 0, "Responses":{0:{"correctness":0,"thinkingPeriod":0,"difficulty":0}}}
updateQuestionHistory(deck=caps_deck,questionID=1,correctness=1,thinkingPeriod=1,difficulty=1)

#print(test)
#print(test["Responses"][1])

if (test["NumOfResponses"]== 1 and 
    test["Responses"][1]["correctness"]==1 and 
    test["Responses"][1]["datestamp"] == datetime.datetime.now()  and
	test["Responses"][1]["thinkingPeriod"] == 1 and
    test["Responses"][1]["difficulty"] == 1):
    print("Test passed")

else: print("Test failed")