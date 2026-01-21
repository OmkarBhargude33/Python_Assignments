def DisplaySqr(No):

    print("Square is : ",(No * No))

def main():

    iValue = 0

    print("Enter the number : ")
    iValue = int(input())

    DisplaySqr(iValue)
    
if __name__ == "__main__":
    main()