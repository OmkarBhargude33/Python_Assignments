def Add(data):
    iSum = 0

    for i in range(len(data)):
        iSum = iSum + data[i]

    return iSum

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

    Ret = Add(data)

    print("Addition is : ",Ret)
        
if __name__ == "__main__":
    main()