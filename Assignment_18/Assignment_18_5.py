import Arithematic

def ListPrime(Arr):
    bRet = False
    iSum = 0

    for i in range(len(Arr)):
        bRet = Arithematic.ChkPrime(Arr[i])
        if(bRet == True):
            iSum = iSum + Arr[i]

    return iSum

def main():
    iSize = 0
    Ret = 0
    data = list()
    iOther = 0

    print("Enter the length of list : ",end="")
    iSize = int(input())

    print("Enter the element in list : ")
    for i in range(iSize):
        Ret = int(input())
        data.append(Ret)

    Ret = ListPrime(data)

    print("Addition of prime elements are : ",Ret)

if __name__ == "__main__":
    main()