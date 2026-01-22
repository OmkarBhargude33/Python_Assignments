# write a program which accepts radius of area and find the area of circle

def AreaOfCircle(Rad):

    PI = 3.14
    Area = PI * Rad * Rad
    return Area
    
def main():

    print("Enter Radius :- ",end="")
    Len = float(input())

    Ret = AreaOfCircle(Len)

    print("Area of Circle is :- ",Ret)

if __name__ == "__main__":
    main()