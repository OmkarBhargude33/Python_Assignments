from functools import reduce

def ChkPrime(iNo):
    if(iNo <= 0):
        return False
    
    bFlag = True
    for i in range(2,(iNo//2 + 1)):
        if(iNo % i == 0):
            bFlag = False
            break
        
    return bFlag


Multiply = lambda iNo: iNo * 2

Maximum = lambda A,B: A if A > B else B

def main():
    data = list()
    iLength = 0
    Ret = 0

    print("Enter length of list :- ",end="")
    iLength = int(input())

    print("Enter the elements in list :- ")
    
    for i in range(iLength):
        Ret = int(input())
        data.append(Ret)

    fData = list(filter(ChkPrime,data))

    mData = list(map(Multiply,fData))

    Ret = reduce(Maximum,mData)

    print("Maximum number is : ",Ret)

if __name__ == "__main__":
    main()