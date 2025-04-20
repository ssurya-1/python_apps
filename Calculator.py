
num1 = float(input("Enter in a number: "))
op = input("Enter in a symbol: ")
num2 = float(input("Enter in a second number: "))

if op == "+":
    print( num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    print(num1 / num2)

else:
    print("Invalid equation")
