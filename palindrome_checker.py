"""
Implementing a Queue Coursework 
By: Arthur Gramlich
Data Structures Section 1
November 3rd, 2024
"""

from collections import deque

def palicheck(pali): 
    dequepali = deque(pali) #initializes the deque

    while len(dequepali) > 1: #goes until there are no characters left
      
        first = dequepali[0]  #get the first element
        last = dequepali[-1]  #get the last element
        
        if first != last: #if they are not the same
            return False

        dequepali.popleft() #removes the first character in the queue after it is checked
        dequepali.pop()     #removes the last character in the queue after it is checked
    return True #if they are the same

pali = input("Please enter a word or phrase. ")

if palicheck(pali): #checks if it is a palindrome
    print (f"{pali} is a palindrome. ")
else:
    print (f"{pali} is not a palindrome. ")
