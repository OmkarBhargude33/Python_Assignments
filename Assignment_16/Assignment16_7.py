# write a program which accepts one parameter and returns true if it is divisible by 5

def Divisible(iNo):
    return iNo % 5 == 0
  
def main():
    iVal = 0

    print("Enter a number : ",end="")
    iVal = int(input())

    bRet = Divisible(iVal)
    
    if(bRet == True):
        print("True")
    else:
        print("False")

if __name__ == "__main__":
    main()