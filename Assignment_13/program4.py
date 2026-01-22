# write a program to print the binary equivalent of that number 

def DisplayBinary(iNo):
    iDigit = 0

    print("Binary Conversion :- ")
    while(iNo != 0):
        iDigit = iNo % 2
        print(iDigit,end="")
        iNo = (iNo // 2)

    print()

def main():
    iValue = 0

    print("Enter the number :- ",end="")
    iValue = int(input())

    DisplayBinary(iValue)

if __name__ == "__main__":
    main()