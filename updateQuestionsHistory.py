import datetime 
from datetime import timedelta

#def updateQuestionHistory(deck,questionHistory,correctness,thinkingPeriod,difficulty):
def updateQuestionHistory(deck,questionHistory,correctness):

	#correctness: 0 incorrect, 1 corect
	#difficulty, value 0-9 0 is too easy 9 is too hard (integer for now but could be float later
	
	# Takes new question response data (timestamp,correctness,thinkingPeriod,difficulty)
	# and updates question history 

	#update box number
	#updateBox(questionHistory,correctness)

	#update next recall time
	#updateNextRecall(questionHistory,box)

	#increment number of responses
    questionHistory["NumOfResponses"] = questionHistory["NumOfResponses"] +1

	#create new response entry
    newResponse = {"correctness":correctness,
                   "datestamp":datetime.datetime.now()}
    
    
    
    #append new response to history
    questionHistory["Responses"].update(
            {questionHistory["NumOfResponses"]:newResponse})
                     
    print(questionHistory["Responses"][1]["correctness"])



#testing function
test = {"NumOfResponses": 0, "Responses":{0:{"correctness":0}}}
updateQuestionHistory(deck=0,questionHistory=test,correctness=1)

#print(test)
print(test["Responses"][1]["datestamp"])

if (test["NumOfResponses"]== 1 and 
    test["Responses"][1]["correctness"]==1 and 
    test["Responses"][1]["datestamp"] == datetime.datetime.now() ) :
	print("Test passed")

else: print("Test failed")