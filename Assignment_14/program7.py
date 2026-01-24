# write a lambda function which accepts one and returns True if it is divisible of 5

Divisible = lambda No: No % 5 == 0

def main():
    
    iValue = 0
    print("Enter the number : ",end="")
    iValue = int(input())

    Ret = Divisible(iValue)

    if(Ret == True):
        print(iValue,"is divisible by 5")
    else:
        print(iValue,"is not divisible by 5")


if __name__ =="__main__":
    main()