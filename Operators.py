# Operators
#Arithmetic Operators are +, -, *,**, /, //, %
while(True):
    n1 = int(input("Enter the First Number\n"))
    op = input("Enter the Operator\n")
    n2 = int(input("Enter the 2nd Number\n"))
    if op == "+":
        print("Result =",n1+n2)
    elif op == "-":
        print("Result =",n1-n2)
    elif op == "*":
        print("Result =",n1*n2)
    elif op =="/":
        print("Result =",n1/n2)
    elif op == "//":
        print("Result =",n1//n2)
    elif op == "**":
        print("Result =",n1**n2)
    elif op == "%":
        print("Result =",n1%n2)
    