
numberA = float(input("Please input 1st Number :"))
numberB = float(input("Please input 2nd Number :"))

def add(x, y):
        result = x + y
        print("The reasult of  addition is ", result)
def subs(x, y):
        result = x - y
        print("The reasult of  Substraction is ", result)
def mul(x, y):
        result = x * y
        print("The reasult of  Multiplication is ", result)
def divide(x, y):
    try:
        result = x / y
        print("The answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

print(" Please enter a operator")
print(" 1 for Addition")
print(" 2 for Substraction")
print(" 3 for Multiplication")
print(" 4 for Division")
choise = input("Enter 1 , 2 ,3 or 4  :")

if choise == "1":
    add(numberA , numberB)
elif choise == "2":
    subs(numberA , numberB)
elif choise == "3":
    mul (numberA , numberB)
elif choise == "4":
    divide(numberA , numberB)
else :
    print("You have given a wrong input")