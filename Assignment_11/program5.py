# write a program which checks whether it is palindrome or not
# I/P :- 121
# O/P :- palindrome

def ChkPalindrome(iNo):
    bFlag = False
    if(iNo < 0):
        return bFlag

    iNew = 0
    iOld = iNo

    while(iNo != 0):
        iDigit = iNo % 10
        iNew = iNew * 10 + iDigit
        iNo = iNo // 10

    if(iNew == iOld):
        bFlag = True

    return bFlag

def main():

    iValue = 0
    bRet = False

    print("Enter the number : ",end="")
    iValue = int(input())

    bRet = ChkPalindrome(iValue)

    if(bRet == True):
        print(iValue,"is Palindrome")
    else:
        print(iValue,"is not a palindrome")

if __name__ == "__main__":
    main()