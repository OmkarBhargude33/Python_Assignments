from functools import reduce

ChkGreater = lambda iNo: iNo if iNo >= 70 and iNo <= 90  else None
        
    
Increase = lambda iNo: iNo + 10

Product = lambda A,B: A * B

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

    fData = list(filter(ChkGreater,data))

    mData = list(map(Increase,fData))

    Ret = reduce(Product,mData)

    print("Product of numbers is : ",Ret)

if __name__ == "__main__":
    main()