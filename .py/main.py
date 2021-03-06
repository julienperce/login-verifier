import os
import sys

readEntries = open(".txt/entries.txt")
entriesFile = open(".txt/entries.txt", "r+")
adminEntriesFile = open(".txt/adminPasswords.txt", "r+")

 
def amtRegUsers():
    numLines = 0
    return len(open(".txt/entries.txt").readlines())

a = int(input("Select your action: 1 to register; 2 to login"))


def regNewUser():
    regUser = input("Choose your username: ")
    regPass = input("Choose your password: ")
    entriesFile.write(regUser)
    entriesFile.write(":")
    entriesFile.write(regPass)
def loginExistingUser():
    loginUser = input("Enter username: ")
    loginPass = input("Enter password: ")
    
    def loginNonAdmin():
        for line in entriesFile:
            valueSplit = line.split(":")
            loggedUser = valueSplit[0]
            loggedPass = valueSplit[1]
            if loginUser == loggedUser and loginPass == loggedPass:
                print("succesful")
    
    def loginAdmin():
        for line in adminEntriesFile:
            valueSplit = line.split(":")
            loggedUser = valueSplit[0]
            loggedPass = valueSplit[1]
            if loginUser == loggedUser and loginPass == loggedPass:
                print("succesful admin login")

    if loginUser == "admin":
        loginAdmin()
    else:
        loginNonAdmin()
    
if a == 1:
    regNewUser()

elif a == 2:
    if os.stat(".txt/entries.txt").st_size == 0:
        print("Error: there are no registered users")
        sys.exit(0) # we pass the arg 0 to make sure it is a "successful termination"; and to not raise an exception
    loginExistingUser()
else:
    print("wrong value")
    sys.exit(0)
    
entriesFile.close()


