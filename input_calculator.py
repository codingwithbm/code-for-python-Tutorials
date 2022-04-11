num1 = int(input("Enter a number: "))
m = input("Enter +,-,x,/  ")
num2 = int(input("Enter another number: "))

if m == "+":
    print(num1 + num2)
elif m == "-":
    print(num1 - num2)
elif m == "x":
    print(num1 * num2)
elif m == "/":
    print(num1 / num2)
else:
    print("ERROR")