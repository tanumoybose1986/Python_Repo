print("welcome to Calculator")


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
choice = input("Enter 1 , 2 ,3 or 4  :")
if choice in ('1', '2', '3', '4'):

 while(True):


  try:
    numberA = float(input("Please input 1st Number :"))
    numberB = float(input("Please input 2nd Number :"))
  except ValueError:
     print("Invalid input. Please enter a number.")
  
  break    

 if choice == "1":
        add(numberA , numberB)
 elif choice == "2":
        subs(numberA , numberB)
 elif choice == "3":
        mul (numberA , numberB)
 elif choice == "4":
        divide(numberA , numberB)
        
else :
        print("You have given a wrong input")   

 





