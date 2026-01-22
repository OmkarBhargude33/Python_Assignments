# write a program which prints the sum of digit
# I/P :- 123
# O/P :- 6

def SumDigit(iNo):
    iSum = 0
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo // 10

    return iSum

def main():

    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    iRet = SumDigit(iValue)

    print("Summation of digit is : ",iRet)

if __name__ == "__main__":
    main()