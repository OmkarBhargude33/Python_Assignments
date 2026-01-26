
def ChkPrime(iNo):
    bFlag = True
    for i in range(2,(iNo//2 + 1)):
        if(iNo % i == 0):
            bFlag = False
            break
        
    return bFlag

def main():

    iVal1 = 0

    print("Enter a number : ",end="")
    iVal1 = int(input())

    Ret = ChkPrime(iVal1)

    if(Ret == True):
        print("It is prime")
    else:
        print("It is not a prime number")


if __name__ =="__main__":
    main()