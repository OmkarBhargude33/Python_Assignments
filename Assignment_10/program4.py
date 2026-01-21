# write a program which accepts one number and print all the even number till that number
# input : 10
# output : 2 4 6 8 10


def DisplayEven(iNo):
    if((iNo < 0) or (iNo == 0)):
        print("Wrong input")
        return

    for i in range(1,iNo+1):
        if(i % 2 == 0):
            print(i)

def main():

    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    DisplayEven(iValue)

if __name__ == "__main__":
    main()