"""
HyperGeometric Calculator without math import
By: Arthur Gramlich
"""

def factorial(n): #function to determine the factorial value
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
    
def combinations(n, k): #calculates the number of combinations
    if k > n or k < 0:
        return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def validate(prompt): #checks if the input is a number, not a word
    while True:
        UserInput = input(prompt)
        if UserInput.isdigit():
            return int(UserInput)
        else:
            print("Invalid input. Please enter a non-negative integer.")
    
SampleName = input("What is the name of your sample? ")
SampleType = input(f"What are you looking for from the {SampleName}? ") 
SampleSize = validate(f"What is the overall amount in the {SampleName}? ") #specific thing you are looking for from the sample
samples = validate(f"How many {SampleType} are in the {SampleName}? ") #the total number that exists within the sample 
chances = validate(f"How many chances do you get at the {SampleType}? ") #the number of times you could see the desired number
successes = validate(f"How many {SampleType} are you looking for from the {SampleName}? ") #the desired number from the sample

successful = combinations(samples, successes)  #chances of drawing the desired amount
failure = combinations(SampleSize - samples, chances - successes)  #chances of not drawing the desired amount
total = combinations(SampleSize, chances)  #total chances of drawing the sample total from the total amount

#Probability calculation, with the chance of being 0
if total > 0:
    probability = ((successful * failure) / total)
else: 
    probability = 0

probabilityPercentage = probability * 100


print(f"There is a {probabilityPercentage:.2f}% chance of drawing {successes} {SampleType} in {chances} chances from the {SampleName}.") 
