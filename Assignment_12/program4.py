def Display(iNo):

   for i in range(1,iNo+1):
    print(iNo)
        
def main():
    iValue = 0

    print("Enter a number :- ",end="")
    iValue = int(input())

    Display(iValue)

if __name__ == "__main__":
    main()