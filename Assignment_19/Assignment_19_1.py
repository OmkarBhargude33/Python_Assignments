Power = lambda No : No * No
def main():

    iValue = 0

    print("Enter a number : ",end="")
    iValue = int(input())

    Ret = Power(iValue)

    print(f"Power of {iValue} is : ",Ret)

if __name__ == "__main__":
    main()