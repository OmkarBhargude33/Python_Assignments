# write a program which accepts one number and check whether it is perfect number or not

def ChkPerfect(iNo):
    bFlag = False
    if(iNo < 1):
        return bFlag

    iSum = 0
    for i in range(1,(iNo//2)+1,1):
        if(iNo % i == 0):
            iSum = iSum + i

    if(iSum == iNo):
        bFlag = True

    return bFlag

def main():

    iValue = 0
    bRet = True

    print("Enter the number :- ",end="")
    iValue = int(input())

    bRet = ChkPerfect(iValue)

    if(bRet == True):
        print(iValue,"is a perfect number")
    else:
        print(iValue,"is not a perfect number")

if __name__ == "__main__":
    main()
