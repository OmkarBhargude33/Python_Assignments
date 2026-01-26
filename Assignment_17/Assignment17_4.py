
def Factors(iNo):
    iFact = 0
    for i in range(1,(iNo//2 + 1)):
        if(iNo % i == 0):
            iFact = iFact + i
    return iFact

def main():

    iVal1 = 0

    print("Enter a number : ",end="")
    iVal1 = int(input())

    Ret = Factors(iVal1)

    print("Addition of factors is : ",Ret)

if __name__ =="__main__":
    main()