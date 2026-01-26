from functools import reduce

ChkEven = lambda iNo: iNo if iNo % 2 == 0 else None
    
Square = lambda iNo: iNo * iNo

Add = lambda A,B:  A + B

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

    fData = list(filter(ChkEven,data))

    mData = list(map(Square,fData))

    Ret = reduce(Add,mData)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()