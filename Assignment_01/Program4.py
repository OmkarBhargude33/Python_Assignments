def DisplayCube(No):

    print("Cube of given number is : ",(No*No*No))

def main():

    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    DisplayCube(iValue)
    
if __name__ == "__main__":
    main()