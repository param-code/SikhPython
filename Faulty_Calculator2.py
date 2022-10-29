# Design a calculator which can input 2 numbers and perform an operation according to the user.
# There must be a fault in the calculator. The fault must be, if the operation performed is 45*3(555), 56+9(77), 56/6=4
# the answer must be given accordingly, as per the brackets corresponding.
print("Welcome to the best calculator you will ever find for your math test!")
a=float(input("Enter your first number:"))
b=float(input("Enter your second number:"))
op=input("Enter the operation you want to perform (+,-,*,/):")
if (a,b)==(45,3) and op=="*":
    print("The answer is:555")
elif (a,b)==(56,9) and op=="+":
    print("The answer is:77")
elif (a,b)==(56,6) and op=="/":
    print("The answer is:4")
else:
    if op=="+":
        print("The answer is:",a+b)
    elif op=="-":
        print("The answer is:",a-b)
    elif op=="*":
        print("The answer is:",a*b)
    elif op == "/":
        print("The answer is:",a/b)
    else:
        print("Enter a valid operation.")