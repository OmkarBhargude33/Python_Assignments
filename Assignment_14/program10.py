# write a lambda function which accepts three number and returns the largest number

Largest = lambda a,b,c: a if a > b and a > c else b if b > a and b > c else c 
def main():
    iValue1 = 0
    iValue2 = 0
    iValue3 = 0
    Ret = 0

    print("Enter first number : ",end="")
    iValue1 = int(input())

    print("Enter second number : ",end="")
    iValue2 = int(input())

    print("Enter third number : ",end="")
    iValue3 = int(input())

    Ret = Largest(iValue1,iValue2,iValue3)

    print("Largest is : ",Ret)

if __name__ =="__main__":
    main()