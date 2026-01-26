
def lenX(iNo):
    iCount = 0
    if(iNo < 0):
        return iCount
    
    while(iNo != 0):
        iCount = iCount + 1
        iNo  = iNo // 10

    return iCount

def main():

    iVal1 = 0

    print("Enter a number : ",end="")
    iVal1 = int(input())

    iRet = lenX(iVal1)

    print("Number of Digits are : ",iRet)

if __name__ =="__main__":
    main()