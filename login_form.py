def loggedin():
    print("Logged in")

    print("(s)how amount of $")
    answer1 = input("")

    if answer1 == "s":
        print("You have 1M $")
    else:
        while True:
            break


print("Select an option (l)ogin | (s)ign up")
answer = input("")

if answer == "s":
    global u
    global p 
    u = input("Create user name: ")
    p = input("Create user password: ")
    print("Account created successfully!")

    print("\nSelect an option (l)ogin | (s)ign up")
    answer = input("")
if answer == "l":
    lu = input("Enter user name: ")

    while lu != u:
        print("User not found")
        lu = input("Enter user name: ")

        

    lp = input("Enter user password: ")

    while lp != p:
        print("Password incorrect")
        lp = input("Enter user password: ")

    loggedin()

    



    
