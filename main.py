
entriesFile = open("entries.txt", "r+")

a = int(input("Select your action: 1 to register; 2 to login"))

if a == 1:
    regUser = input("Choose your username: ")
    regPass = input("Choose your password: ")
    entriesFile.write(regUser)
    entriesFile.write(":")
    entriesFile.write(regPass)
elif a == 2:
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
else:
    print("wrong value")