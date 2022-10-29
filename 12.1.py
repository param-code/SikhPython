# Program that Keeps on taking number until user Enter a 3 Digit number
i = 0
while(True):
    i = i + 1
    print("Enter the Number")
    n = int(input())
    if n > 99:
        break
