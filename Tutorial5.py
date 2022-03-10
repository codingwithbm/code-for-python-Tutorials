# while loop

password = input("Create a password ")
enter_password = input("Enter a password ")

while password != enter_password:
    print("Wrong password! ")
    enter_password = input("Enter a password ")

print("Correct password! ")
