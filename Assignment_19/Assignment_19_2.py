Multiplication = lambda No1,No2 : No1 * No2
def main():

    iValue1 = 0
    iValue2 = 0

    print("Enter first number : ",end="")
    iValue1 = int(input())

    print("Enter second number : ",end="")
    iValue2 = int(input())

    Ret = Multiplication(iValue1,iValue2)

    print(f"{iValue1} * {iValue2} is : ",Ret)

if __name__ == "__main__":
    main()