import math
Options=["1.Square","2.Rectangle","3.Circle","4.Triangle"]
print(*Options,end="\n")

while (True):
    op=int(input("Enter the Option: "))
    if op==1:
        print("___________For Square______________")
        side=abs(int(input("Enter the side of the square: ")))
        print("_______Area of the Square is:",side*side,"_________")
    elif op==2:
        print("__________For Rectangle_____________")
        length=abs(int(input("Enter the length of the Rectangle: ")))
        width=abs(int(input("Enter the width of the Rectangle: ")))
        print("_______Area of the Reactangle is:",length*width,"_________")
    elif op==3:
        print("__________For Circle_______________")
        radius=abs(int(input("Enter the radius of the Circle: ")))
        print("_______Area of the Circle is:",math.pi*radius,"_________")
    elif op==4:
        print("_________For Triangle______________")
        base=abs(int(input("Enter the base of the Triangle: ")))
        height=abs(int(input("Enter the height of the Triangle: ")))
        print("_______Area of the Circle is:",  (base*height)/2 ,"_________")
    else:
        print("Wrong option selected")
        break
