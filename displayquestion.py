# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 08:57:22 2020

@author: Woody
"""
import json
import random
import time
#4import timeit

#print(random.randrange(4))



with open('data.json', 'r') as fp:
    questions = json.load(fp)
    

    
def askQuestion(source, number):  #interface after card selector
    print(source['pack']['baseQ'], end = '')
    print(source[number]['card']['question'], end = '')
    print(':')
    position = random.randrange(4)
    for i in range(4):
        print(i+1, end = '')
        print(": ", end = '')
        if (i == position):
            print(source[number]['card']['answer'])
        else:
            print(getRandomAnswer(source, number))
    return(position+1)
    
def getRandomAnswer(source, number):  #pulls a random answer from elsewhere on the card to fill out the multiple choice
    card=random.choice(list(source.keys()))
    #print(card)
    if ((card==number) or not(card.isdigit())):  #only accept answer if its a diferent, valid, card
        return getRandomAnswer(source, number)
    else:
        return source[card]['card']['answer']
        
def checkAnswer(answer):
    startT=time.time()
    response=input("")
    while not(response.isdigit()):
        response=input("Please type a number: ")
    questionT=time.time()-startT
    if int(response)==answer:
        print("Correct!")
        return 1, questionT
    else: 
        print("Wrong!")
        return 0, questionT
    

def askDifficulty():
    
    response=input("How easy was that?\n0:Too easy\n3:Knew it\n7:Wasn't sure\n9: complete guess")
    while not(response.isdigit()):
        response=input("Please type a number 0-9:")
    
    response=int(response)
    if (response<0): response=0
    if (response>9): response=9
    return response
    

#

position=askQuestion(questions,str(random.randrange(200)))
#
#print(questionT)
checkA=checkAnswer(position)

print(askDifficulty())




print("that took you: ", end = '')
print("%.1lf" % questionT, end = '')
print(" seconds")
