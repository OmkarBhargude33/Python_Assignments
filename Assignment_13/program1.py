# write a program which accepts length and width and find the area of rectangle


def Area(Length, Width):

    Area = Length * Width

    return Area

def main():

    print("Enter length :- ",end="")
    Len = float(input())

    print("Enter width :- ",end="")
    Wid = float(input())

    Ret = Area(Len,Wid)

    print("Area of rectangle is :- ",Ret)

if __name__ == "__main__":
    main()