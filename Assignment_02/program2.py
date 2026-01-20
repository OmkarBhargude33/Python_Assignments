# write a program which accepts one number and print the sum of first N natural numbers.
# input : 5
# output : 15

def Table(iNo):
    if((iNo < 0) or (iNo == 0)):
        print("Wrong input")
        return

    iSum = 0
    for i in range(1,iNo+1):
        iSum = iSum + i

    print("Sumation of natural number is : ",iSum)

def main():

    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    Table(iValue)

if __name__ == "__main__":
    main()