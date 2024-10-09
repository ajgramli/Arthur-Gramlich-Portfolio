"""
Counting Program Coursework
By AJ Gramlich
"""
x = input ("Please enter a statement.")

vowels = 0
spaces = 0
upper = 0
lower = 0
number = 0
symbol = 0

for c in x:
    if c in 'AEIOUaeiou':
        vowels += 1
    elif 'A' <= c <= 'Z':
        upper += 1
    elif 'a' <= c <= 'z':
        lower += 1
    elif c == ' ':
        spaces += 1
    elif '0' <= c <= '999':
        number += 1

    else:
        symbol += 1

print ("There are", vowels, "Vowels")
print ("There are",upper, "upper case letters")
print ("There are",lower, "lower case letters")
print ("There are", spaces, "Spaces")
print ("There are", number, "numbers")
print ("There are",symbol,  "symbols")
