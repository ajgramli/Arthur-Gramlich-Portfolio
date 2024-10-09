"""
Arthur Gramlich
Data Structures Section 1
September 29th, 2024
"""

height = 0
weight = 0
bmi = 0

BmiValues = [] #list of BMI Values
names = ["Steve", "Tony", "Natasha", "Bruce", "Peter", "Bucky"] #names of participants
categories = {"Underweight": 0, "Normal Weight": 0, "Overweight": 0} #initializes categories for weight

def BmiCalc(weight, height): #BMI calculation
    return (weight * 703) / (height ** 2) 

for name in names: #loops each name in list to have their BMI calculated
    weight = float(input(f"Enter weight in pounds for {name}: "))
    height = float(input(f"Enter height in inches for {name}: "))
    
    bmi = BmiCalc (weight, height)
    BmiValues.append(bmi) #appends each person to their weight category
    
    if bmi < 18.5: #Categorizes participants based on their BMI
        categories["Underweight"] += 1
    elif 18.5 <= bmi < 24.9:
        categories["Normal Weight"] += 1
    else:
        categories["Overweight"] += 1
    
for i in range(len(names)): #for each name in the list, it will output the proper BMI value 
    print(f"{names[i]}: {BmiValues[i]:.2f}")

for category, count in categories.items(): #for each category in the dictionary, it will output the total people
    print(f"{category}: {count}")