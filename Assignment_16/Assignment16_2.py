# write a function ChkNum() which accepts one parameter and if number is even the it should display even else odd


def ChkNum(iNo):
    if(iNo % 2 == 0):
        print("Even Number")
    else:
        print("Odd Number")

def main():
    iVal = 0

    print("Enter a number : ",end="")
    iVal = int(input())

    ChkNum(iVal)
        
if __name__ == "__main__":
    main()