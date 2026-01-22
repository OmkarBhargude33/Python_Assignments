def Display(iNo):

    while(iNo != 0):
        print(iNo)
        iNo = iNo - 1
        
def main():
    iValue = 0

    print("Enter a number :- ",end="")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()