# Basic Area Calculator
def square_area():
    sqside = float(input("enter side:\n"))
    if sqside == 0:
        print("value should be more than zero")
        return
    sq_area = sqside ** 2
    print("Area of Square is :", sq_area)
    return sq_area


def rectangle_area():
    b = float(input("enter first side\n"))
    h = float(input("enter second side\n"))
    if b == 0 and h == 0:
        print("value should be more than zero")
        return
    rec_area1 = b * h
    print("Area of Rectangle is", rec_area1)
    return rec_area1


def circle_area():
    r = int(input("enter radius\n"))
    circ_area1 = 3.142 * r * r
    print("Area of Circle is", circ_area1)
    return circ_area1


sq = square_area
ci = circle_area
re = rectangle_area

print("Choose your entity\n", "sq for square\n", "re for rectangle\n", "ci for circle")
ans = input("Enter entity to find area\n")

while (ans):
    if ans == "sq":
        print(square_area())
        break
    if ans == "ci":
        print(circle_area())
        break
    if ans == "re":
        print(rectangle_area())
        break
    else:
        print("Wrong entity")
        break
