# write a lambda function which accepts two number and returns the maximum number

Maximum = lambda a,b: a if a > b else b  

def main():
    iValue1 = 0
    iValue2 = 0
    Ret = 0

    print("Enter first number : ",end="")
    iValue1 = int(input())

    print("Enter second number : ",end="")
    iValue2 = int(input())

    Ret = Maximum(iValue1,iValue2)

    print("Maximum is : ",Ret)

if __name__ =="__main__":
    main()