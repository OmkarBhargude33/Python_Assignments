
def Display(iNo):

    for i in range(iNo):
        print("* ",end="")
    print()

def main():
    iVal = 0

    print("Enter a number : ",end="")
    iVal = int(input())

    Display(iVal)

if __name__ == "__main__":
    main()