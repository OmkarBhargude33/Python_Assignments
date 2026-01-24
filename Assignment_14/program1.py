# write a lambda function which accepts one and returns the square of that number 

sqaure = lambda No : No * No

def main():

    iValue = 0
    print("Enter the number : ",end="")
    iValue = int(input())

    Ret = sqaure(iValue)

    print("Sqaure is : ",Ret)
    
if __name__ == "__main__":
    main()