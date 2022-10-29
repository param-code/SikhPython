# Program to Guess the number in Limited Trials!
n = 19
i = 0
while (True):
    i = i + 1
    if i > 10:
        print("Game Over")
        break
    print("No of Trials Left =",i - 11)
    print("Guess the Number")
    a = int(input())
    if a > n:
        print("Your Number Is Greater")
    elif a < n:
        print("Your Number is Smaller")
    elif a == n:
        print("Wow! Tussi Jaadugar Ho Jii!!")
        break
