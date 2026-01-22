# write a program which accepts one number and checks if it prime or not

def ChkPrime(iNo):
    if(iNo <= 1):
        return False

    bFlag = True

    for i in range(2,iNo//2 + 1):
        if(iNo % i == 0):
            bFlag = False
            break
    
    return bFlag

def main():

    iValue = 0
    bRet = True

    print("Enter the number : ",end="")
    iValue = int(input())

    bRet = ChkPrime(iValue)

    if(bRet == False):
        print(iValue,"is not a prime number")
    else:
        print(iValue,"is a prime number")

if __name__ == "__main__":
    main()