
def AddDigits(iNo):
    add = 0
    if(iNo < 0):
        return add
    
    while(iNo != 0):
        iDigit = iNo % 10 
        add = add + iDigit
        iNo  = iNo // 10

    return add

def main():

    iVal1 = 0

    print("Enter a number : ",end="")
    iVal1 = int(input())

    iRet = AddDigits(iVal1)

    print("Addition of digit is : ",iRet)

if __name__ =="__main__":
    main()