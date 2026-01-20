#write a program which accepts one number and print the factorial of that numbers.
# input : 5
#output : 120

def Factorial(iNo):
    if((iNo < 0) or (iNo == 0)):
        print("Wrong input")
        return

    iFact = 1
    for i in range(1,iNo+1):
        iFact = iFact * i

    print("Factorial of number is : ",iFact)

def main():

    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    Factorial(iValue)

if __name__ == "__main__":
    main()