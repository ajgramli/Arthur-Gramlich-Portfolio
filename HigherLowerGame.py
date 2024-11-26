"""
Higher or Lower Card Game Project
By: Arthur Gramlich
"""

import random

class Card: #creates cards in the deck
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
    def __str__(self):
        if self.value in facevalues:
            return f"{facevalues[self.value]} of {self.suit}"
        else:
            return f"{self.value} of {self.suit}"
    
    #Comparison Operations
    def __gt__(self, other):
        return self.value > other.value
    def __lt__(self, other):
        return self.value < other.value
    def __eq__(self, other):
        return self.value == other.value
    def __repr__(self):
        return f"{self.value} of {self.suit}"

def getguess(): #retrieves user's guess
    while True:
        guess = input (f"Will the next card be higher or lower than {randomCard}? ")
        if guess in ('higher', 'h', 'lower', 'l'):
            return guess
        else:
            print("Invalid input. Please enter higher or lower. ")

values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] #card values
suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades'] #card suits
facevalues = {11: "Jack", 12: "Queen", 13: "King", 14: "Ace"} #converts higher numbers to face cards
deck = [Card(value, suit) for value in values for suit in suits] #creates deck of cards
guesses = 0 #tracks all guesses
correct = 0 #tracks correct guesses
wrong = 0 #tracks wrong guesses
start = (input("Welcome to Higher or Lower, a game that presents a random card from a deck and you must decide if the next card will be higher or lower. \nPress y to play or any other button to exit. "))

if start =='y':
    random.shuffle(deck)
    randomCard = deck.pop() #gets card from top of the deck 
    print(f"Your card is {randomCard}. ") #presents card from the top of the deck
    
    while len(deck) > 0: #goes until deck is empty
        nextCard = deck.pop()
        guess = getguess()
        guesses += 1
        
        if (guess == 'higher' or guess == 'h') and nextCard > randomCard: #if the next card is higher and the guess was higher
            correct += 1
            print(f"Correct! The next card is {nextCard}. \nGuesses: {guesses} \nCorrect: {correct} \nIncorrect: {wrong}")
        elif (guess == 'lower' or guess == 'l') and nextCard < randomCard: #if the next card is lower and the guess was lower
            correct += 1
            print(f"Correct! The next card is {nextCard}. \nGuesses: {guesses} \nCorrect: {correct} \nIncorrect: {wrong}")
        else: #if the guess is wrong
            wrong += 1
            print(f"Incorrect! The next card is {nextCard}. \nGuesses: {guesses} \nCorrect: {correct} \nIncorrect: {wrong}")
        randomCard = nextCard #goes to next card in deck
        print (f"Cards In Deck: {len(deck)}")
    
    print("\nGame Over! Final Results: ") #shows results once the game is over
    print(f"Total Guesses: {guesses}, Correct: {correct}, Incorrect: {wrong}")
    
else:
    exit()
