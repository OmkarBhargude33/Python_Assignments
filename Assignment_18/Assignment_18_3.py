def Minimum(Arr):
    Min = Arr[0]

    for i in range(len(Arr)):
        if(Min > Arr[i]):
            Min = Arr[i]

    return Min

def main():
    iSize = 0
    Ret = 0
    data = list()

    print("Enter the length of list : ")
    iSize = int(input())

    print("Enter the element in list : ")
    for i in range(iSize):
        Ret = int(input())
        data.append(Ret)

    Ret = Minimum(data)

    print("Minimum element is  : ",Ret)
        
if __name__ == "__main__":
    main()