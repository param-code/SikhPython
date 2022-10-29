#Program for a Faulty Calculator
print("Enter 1st Number")
n1 = int(input())
print("Enter the Operator")
op = input()
print("Enter 2nd Number")
n2 = int(input())
if op == "+":
    print(n1+n2)
elif op == "-":
    print(n1-n2)
elif op == "*":
    print(n1*n2)
elif op == "/":
    print(n1/n2)
else:
    print("Please! Choose Appropriate Operator")
