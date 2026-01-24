# write a lambda function which accepts one and returns True if it Even

Even = lambda No: No % 2 == 0

def main():
    
    iValue = 0
    print("Enter the number : ",end="")
    iValue = int(input())

    Ret = Even(iValue)

    if(Ret == True):
        print("It is Even")
    else:
        print("It is Odd")

if __name__ =="__main__":
    main()