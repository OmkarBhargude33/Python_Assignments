# write a program which accepts one parameter and check whether it is positive or not

def ChkPositive(iNo):
    bFlag1 = True
    
    if(iNo < 0):
        bFlag1 = False
    

    return bFlag1    
def main():
    iVal = 0

    print("Enter a number : ",end="")
    iVal = int(input())

    bRet1 = ChkPositive(iVal)
    
    if(bRet1 == True):
        print("Positive number")
    else:
        print("Negative number")

if __name__ == "__main__":
    main()