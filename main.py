import os
import sys

readEntries = open("entries.txt")
entriesFile = open("entries.txt", "r+")

def amtRegUsers():
    numLines = 0
    return len(open("entries.txt").readlines())
print(f"there are currently {amtRegUsers()} users registered.")
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
    for line in entriesFile:
        valueSplit = line.split(":")
        loggedUser = valueSplit[0]
        loggedPass = valueSplit[1]
        if loginUser == loggedUser and loginPass == loggedPass:
            print("succesful")
        else:
            print("failure")

if a == 1:
    regNewUser()

elif a == 2:
    if os.stat("entries.txt").st_size == 0:
        print("Error: there are no registered users")
        sys.exit(0) # we pass the arg 0 to make sure it is a "successful termination"; and to not raise an exception
    loginExistingUser()
else:
    print("wrong value")
    sys.exit(0)