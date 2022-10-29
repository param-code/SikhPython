# program to create a list and using for Loop Print only Numbers > 6
L = ["Rohan", "Raja", "Alice", "Chai", 50, 48, -4, 5, 16]
for item in L:
    if type(item)==int and item > 6:
        print(item)
