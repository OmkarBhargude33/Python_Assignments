def ChkGreater(No1,No2):

    if(No1 > No2):
        print(No1)
    else:
        print(No2)

def main():

    iValue1 = 0
    iValue2 = 0

    print("Enter numbers : ")
    iValue1 = int(input())
    iValue2 = int(input())

    ChkGreater(iValue1,iValue2)

if __name__ == "__main__":
    main()