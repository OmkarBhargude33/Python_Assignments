# write a lambda function which accepts one and returns the cube of that number 

cube = lambda No : No * No * No

def main():
    iValue = 0
    print("Enter the number : ",end="")
    iValue = int(input())

    Ret = cube(iValue)

    print("cube is : ",Ret)

if __name__ =="__main__":
    main()