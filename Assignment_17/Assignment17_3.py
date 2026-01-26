
def Factorial(iNo):
    iFact = 1
    for i in range(1,iNo+1):
        iFact = iFact * i

    return iFact

def main():

    iVal1 = 0

    print("Enter a number : ",end="")
    iVal1 = int(input())

    Ret = Factorial(iVal1)

    print("Factorial is : ",Ret)

if __name__ =="__main__":
    main()