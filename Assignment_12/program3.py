# write a program which accepts two number and print it addition, substraction 
# multiplication and division

def DisplayArithmetic(iNo1, iNo2):
    
    print("Addition is :- ",iNo1 + iNo2)
    print("Substraction is :- ",iNo1 - iNo2)
    print("Multiplication is :- ",iNo1 * iNo2)
    print("Division is :- ",iNo1 // iNo2)

def main():

    iValue1 = 0
    iValue2 = 0

    print("Enter first number :- ",end="")
    iValue1 = int(input())

    print("Enter second number :- ",end="")
    iValue2 = int(input())

    DisplayArithmetic(iNo1 = iValue1, iNo2 = iValue2)

if __name__ == "__main__":
    main()