"""
Username Generator
By: Arthur Gramlich
"""

loginList = []
admin = "Arthur"

def generator (first, last, name): #creates the username
    firstLetter = first [0] #takes first letter of the name
    username = firstLetter + last #combines first letter of the name to the last name
    totalUsers = 1
    if any (username in entry for entry in loginList): #checks if username exists
        while any (username in entry for entry in loginList): #Keep checking until unique
            username = f"{firstLetter}{last}{totalUsers}" #Append a number to the username
            totalUsers += 1
 
    loginList.append(f"{name}: {username}") #adds the user to the list
    print (f"The username is {username}. ")
    
def adminAccess(admin): #admin access to create multiple usernames
    adminID = input ("If you are an Admin, please enter your admin ID to access the list of usernames. If you are not an admin, type exit. ")
    if adminID == admin: #grants admin access
        print ("Access Granted. ")
        print (loginList) #only admins can check the list of usernames 
        return True #only admins can create multiple usernames
    elif adminID == "exit":
        return False
    else:
        print ("Invalid ID. Access denied. ") 
        return False
    
while True:
    first = input("What is the user's first name? (or type 'exit' to quit): ").lower() #gets user's first name
    if first == "exit":
        print("Exiting program. ")
        break
    last = input("What is the user's last name? ").lower() #gets user's last name
    name = f"{first.upper()} {last.upper()}"

    generator(first, last, name) #create the username
    isAdmin = adminAccess(admin) #checks for admin access
    if not isAdmin:
        print ("Only admin users can create multiple usernames. Exiting Program. ")
        exit()
