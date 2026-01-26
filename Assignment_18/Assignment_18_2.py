def Maximum(Arr):
    Max = Arr[0]

    for i in range(len(Arr)):
        if(Max < Arr[i]):
            Max = Arr[i]

    return Max

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

    Ret = Maximum(data)

    print("Maximum element is  : ",Ret)
        
if __name__ == "__main__":
    main()