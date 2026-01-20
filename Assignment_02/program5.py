# write a program which accepts one number and print all the odd number till that number
# input : 10
# output : 1 3 5 7 9

def DisplayOdd(iNo):
    if((iNo < 0) or (iNo == 0)):
        print("Wrong input")
        return

    for i in range(1,iNo+1):
        if(i % 2 != 0):
            print(i)

def main():

    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    DisplayOdd(iValue)

if __name__ == "__main__":
    main()