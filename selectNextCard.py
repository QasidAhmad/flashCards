import random
import time

def selectNextCard(deck, method="default"):
    
    maxBoxes=8  #the naximum number of boxes available
    
	# select next card based on history of reponses
    
    # simulating card selection with random selection
    if (method=="random"):
        nextCardID = random.randrange(200)
    elif (method=="default"):
        
        #search through unseen cards frist and choose randomly
        unseenCards=[] 
        for card in deck['deck']:
            if deck['deck'][card]['history']['box']==0:
                unseenCards.append(card)
        if len(unseenCards)>0:
            nextCardID=random.choice(unseenCards)
            return nextCardID
        #then find most overdue cards in each box 1 onwards...
        for level in range(1,maxBoxes):
            mostOverDue=""
            recallTime=time.time()
            for card in deck['deck']:
                if deck['deck'][card]['history']['box']==level:
                    if deck['deck'][card]['history']['nextRecall']<recallTime:
                        recallTime=deck['deck'][card]['history']['nextRecall']
                        mostOverDue=card
            if not(mostOverDue==""):
                return card
        #then find card which will become overdue soonest... (makes last section a little redundent)
        for level in range(1,maxBoxes):
            mostOverDue=""
            recallTime=time.time()+60*60*24*365*5
            for card in deck['deck']:
                if deck['deck'][card]['history']['box']==level:
                    if deck['deck'][card]['history']['nextRecall']<recallTime:
                        recallTime=deck['deck'][card]['history']['nextRecall']
                        mostOverDue=card
            if not(mostOverDue==""):
                return card
            
    elif (method=="newlast"):
        
        
        #find most overdue cards from box 1 onwards...
        for level in range(1,maxBoxes):
            mostOverDue=""
            recallTime=time.time()
            for card in deck['deck']:
                if deck['deck'][card]['history']['box']==level:
                    if deck['deck'][card]['history']['nextRecall']<recallTime:
                        recallTime=deck['deck'][card]['history']['nextRecall']
                        mostOverDue=card
                        
            if not(mostOverDue==""):
                return mostOverDue
        #search through unseen cards frist and choose randomly
        unseenCards=[] 
        for card in deck['deck']:
            if deck['deck'][card]['history']['box']==0:
                unseenCards.append(card)
        if len(unseenCards)>0:
            nextCardID=random.choice(unseenCards)
            return nextCardID
        #then find card which will become overdue soonest...
        for level in range(1,maxBoxes):
            mostOverDue=""
            recallTime=time.time()+60*60*24*365*5
            for card in deck['deck']:
                if deck['deck'][card]['history']['box']==level:
                    if deck['deck'][card]['history']['nextRecall']<recallTime:
                        recallTime=deck['deck'][card]['history']['nextRecall']
                        mostOverDue=card
            if not(mostOverDue==""):
                return card
            
       # nextCardID="1"
    
    return nextCardID  #returns string of next card ID

#test =1 
#print(selectNextCard(test))