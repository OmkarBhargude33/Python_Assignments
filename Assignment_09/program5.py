def CheckDivisible(No):

    bFlag = False

    if((No % 3 == 0) and (No % 5 == 0)):
        bFlag = True

    return bFlag

def main():

    iValue = 0
    bRet = False

    print("Enter the number : ",end="")
    iValue = int(input())

    bRet = CheckDivisible(iValue)

    if(bRet == True):
        print("It is divisible by 3 & 5")
    else:
        print("It is not divisible by 3 & 5")

if __name__ == "__main__":
    main()