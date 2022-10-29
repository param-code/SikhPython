#Program for a Faulty Calculator that Calculates Every thing Correct few i.e. 45*3=555 or 56+9=77 or 56/6=4
print("Welcome to the Best Calculator For the Math Test")
print("Enter 1st Number")
a = int(input())
print("Enter 2nd Number")
b = int(input())
print("Please Enter a Valid Operator")
op = input()
if (a,b)==(45,3) and op == "*":
    print(555)
elif (a,b)==(56,9) and op == "+":
    print(77)
elif(a,b)==(56,6) and op =="/":
    print(4)
else:
    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op =="*":
        print(a*b)
    elif op=="/":
        print(a/b)
print("Dhanyawaad!!")
