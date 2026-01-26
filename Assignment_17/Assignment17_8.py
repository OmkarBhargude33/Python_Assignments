
def Pattern(iNo):
    for i in range(1,iNo+1):
        for j in range(1,iNo+1):
            if(i >= j):
                print(j," ",end="")
        print()


def main():

    iVal1 = 0

    print("Enter a number : ",end="")
    iVal1 = int(input())

    Pattern(iVal1)

if __name__ =="__main__":
    main()