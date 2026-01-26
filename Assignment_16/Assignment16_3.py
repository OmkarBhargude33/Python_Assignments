# write a function Add() which accepts two parameter and return the addition


def Add(No1,No2):
    return No1 + No2

def main():
    iVal1 = 0
    iVal2 = 0

    print("Enter a first : ",end="")
    iVal1 = int(input())

    print("Enter a second : ",end="")
    iVal2 = int(input())

    iRet = Add(iVal1,iVal2)

    print("Addition is : ",iRet)
    
if __name__ == "__main__":
    main()