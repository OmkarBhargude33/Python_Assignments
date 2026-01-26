def Frequency(Arr,iNo):
    iFreq = 0

    for i in range(len(Arr)):
        if(Arr[i] == iNo):
            iFreq = iFreq + 1

    return iFreq

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

    print("Enter the number to check the frequency : ",end="")
    iOther = int(input())

    Ret = Frequency(data,iOther)

    print(f"Frequency of {iOther} is  : ",Ret)
        
if __name__ == "__main__":
    main()