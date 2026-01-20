# write a program which accepts one number and print multiplication table of that number
# input : 2
# output : 2 4 6 8 10 12 14 16 18 20

def DisplayTable(iNo):
    if((iNo < 0) or (iNo == 0)):
        print("Wrong input")
        return

    for i in range(1,11):
        print(iNo * i)


def main():

    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    DisplayTable(iValue)

if __name__ == "__main__":
    main()