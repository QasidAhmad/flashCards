import random

def selectNextCard(questionsHistory):

	# select next card based on history of reponses
    
    # simulating card selection with random selection
    nextCardID = random.randrange(200)
	
    return nextCardID

#test =1 
#print(selectNextCard(test))