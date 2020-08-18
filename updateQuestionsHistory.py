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
    newResponse = {"correctness":1,"datestamp":datetime.datetime.now()}
    
    questionHistory["Responses"].update(
            {questionHistory["NumOfResponses"]:newResponse})
                    #[("correctness",correctness),
                     #("timestamp",1)]})
		#time of response
	#questionHistory["Responses"]["NumOfResponses"]["timestamp"] = datetime.now()
		#thinking period of response
	#questionHistory["Responses"]["NumOfResponses"]["thinkingPeriod"] = thinkingPeriod
		#correctness of response
	#questionHistory["Responses"]["NumOfResponses"]["correctness"] = correctness
		#difficult of response (to question)
	#questionHistory["Responses"]["NumOfResponses"]["difficulty"] = difficulty


#testing function
test = {"NumOfResponses": 0, "Responses":{0:{"correctness":0}}}
updateQuestionHistory(deck=0,questionHistory=test,correctness=1)

#print(test)
print(test["Responses"][1]["datestamp"])

#if test["NumOfResponses"]== 1 and test["Responses"]["correctness"]==1:
#	print("Test passed")

#else: print("Test failed")