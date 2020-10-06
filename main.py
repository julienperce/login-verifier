registeredLogins = {}
a = int(input("Select your action: 1 to register; 2 to login"))
if a == 1 or a == 2:
    newRegUser = input("Choose your username: ")
    newRegPass = input("Choose your password: ")
    registeredLogins[newRegUser] = newRegPass
else: 
    print("wrong input")

print(registeredLogins)