# flashCards#

Purpose:
Flash Card application aiming to accelerate learning by spaced repetition. 
Creates a deck of cards, each containing a question and corresponding answer to learn.
In the current example, the questions and answers are countries and their corresponding capital cities.

What it does:
The cards are presented to the user one at a time. 
The response of the user to the card presented is recorded.
Each next card presented to the user is selected based on previous reponses. Cards which the user answers incorrectly are recalled more frequently than those which are answered correctly.

How it works:
A deck of cards is imported from a CSV file input by the user. 
The deck exists as a Python dictionary during run time and is stored as a json file for persistence.
The user is initially prompted to select a deck and then presented with a card's question from that deck.
The user is then prompted to specify how difficult they found the question. 
The time that the user spends trying to answer the question is automatically recorded. 
Whether the users reponse to the answer is correct, their thinking time and difficulty rating is recorded in the deck as history associated with each card for each response.  
Each time the user repsonds, the priority of that card for subsequent recall is updated by updating its 'box' property.
The 'box' is a reference to the Leitner system for spaced repetition where flash cards are moved between boxes with associated spacing intervals depending on their recall success i.e. if a card is answered correctly then it is moved to a higher level box which is requires is to be recalled after a longer time period whereas if it is answered incorrectly it is moved to a lower level box, the cards in which are required to be recalled after a shorter period. 
A session ends when either:
1) The number of cards initially specified have been completed;
2) The users forces an exit by entering exit???
3) All the cards required to be recalled have already been reviewed i.e. no call recall times are due???