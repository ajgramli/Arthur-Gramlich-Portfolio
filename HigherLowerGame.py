"""
Higher or Lower Deck Game
By: Arthur Gramlich
"""

import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        if self.value in facevalues:
            return f"{facevalues[self.value]} of {self.suit}"
        else:
            return f"{self.value} of {self.suit}"
    
    def __gt__(self, other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value
    def __repr__(self):
        return f"{self.value} of {self.suit}"

def getguess():
    while True:
        guess = input (f"Will the next card be higher or lower than {randomCard}? ")
        if guess in ('higher', 'h', 'lower', 'l'):
            return guess
        else:
            print("Invalid input. Please enter higher or lower. ")

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] 
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
facevalues = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"}
deck = [Card(value, suit) for value in values for suit in suits]
guesses = 0
correct = 0
wrong = 0
start = (input("Welcome to Higher or Lower, a game that presents a random card from a deck and you must decide if the next card will be higher or lower. \nPress y to play or any other button to exit. "))

if start =='y':
    random.shuffle(deck)
    randomCard = deck.pop()
    print(f"Your card is {randomCard}. ")  
    
    while len(deck) > 0:
        nextCard = deck.pop()
        guess = getguess()
        guesses += 1
        
        if (guess == 'higher' or guess == 'h') and nextCard > randomCard:
            correct += 1
            print(f"Correct! The next card is {nextCard}. \nGuesses: {guesses} \nCorrect: {correct} \nIncorrect: {wrong}")
        elif (guess == 'lower' or guess == 'l') and nextCard < randomCard:
            correct += 1
            print(f"Correct! The next card is {nextCard}. \nGuesses: {guesses} \nCorrect: {correct} \nIncorrect: {wrong}")
        else:
            wrong += 1
            print(f"Incorrect! The next card is {nextCard}. \nGuesses: {guesses} \nCorrect: {correct} \nIncorrect: {wrong}")
        randomCard = nextCard
        print (f"Cards In Deck: {len(deck)}")
    
    print("\nGame Over! Final Results: ")
    print(f"Total Guesses: {guesses}, Correct: {correct}, Incorrect: {wrong}")
    
else:
    exit()
