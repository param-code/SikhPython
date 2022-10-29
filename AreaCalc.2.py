#In This One WE will take input and Calculate the Area
def Circle():
    r = float(input("Enter The Radius\n"))
    area = (22/7)*(r*r)
    return area

def Square():
    s = float(input("Enter the Side Of the Square\n"))
    area = s*s
    return area

def Rectangle():
    s = float(input("Enter the Length\n"))
    t = float(input("Enter the Breadth\n"))
    area = s*t
    return area

while(True):
    print("Type s for SQUARE , c for CIRCLE ,r for RECTANGLE")
    i = input()
    if i == "c" :
        print(Circle())
    elif i == "s":
        print(Square())
    elif i == "r":
        print(Rectangle())
    elif i == "EXIT":
        break
    else:
        print("Thik se DEKH Bhai!!")
