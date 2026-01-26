
def DisplayLen(ch):
    iCount = 0

    for c in ch:
        iCount = iCount+1
        
    print("Length is : ",iCount)

def main():

    print("Enter your name : ",end="")
    cName = input()

    DisplayLen(cName)

if __name__ == "__main__":
    main()