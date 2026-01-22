# write a code which accepts one number and count the number of digits
# I/P :- 7821   
# O/P :- 4

def CountDigit(iNo):
    iCount = 0

    while(iNo != 0):
        iCount += 1
        iNo = iNo // 10

    return iCount

def main():

    iValue = 0
    iRet = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    iRet = CountDigit(iValue)

    print("Number digits are : ",iRet)

if __name__ == "__main__":
    main()