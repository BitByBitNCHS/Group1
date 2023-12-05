num_1 = float(input("First Number: "))
num_2 = float(input("Second Number: "))
Operator = input("Select an operator: ")


def Divide():
    print(num_1 / num_2)


def Mult():
    print(num_1 * num_2)


def Sub():
    print(num_1 - num_2)


def Add():
    print(num_1 + num_2)


if Operator == "-":
    Sub()
elif Operator == "+":
    Add()
elif Operator == "/":
    Divide()
elif Operator == "*":
    Mult()
else:
    print("Wrong Inputs!! Try Again!!")
