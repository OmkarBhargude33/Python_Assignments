
def Pattern(iNo):
    for i in range(1,iNo+1):
        for j in range(iNo,0,-1):
            if(i <= j):
                print("* ",end="")
        print()


def main():

    iVal1 = 0

    print("Enter a number : ",end="")
    iVal1 = int(input())

    Pattern(iVal1)

if __name__ =="__main__":
    main()