# Program to Print If one is Eligible To Drive or not
print("Please , Enter Your Age")
Age = int(input())
if Age < 7 or Age > 100:
    print("Marna Hai Kya Bhai!!")
elif Age < 18:
    print("You Can't Drive Right Now")
elif Age > 18:
    print("Congratutions! You're Eligible to Drive so Please Come as Soon As Possible")
else:
    print("Aana Padege Beta!")
