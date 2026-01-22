# write a program which prints the reverse of that number
# I/P :- 123
# O/P :- 321

def ReverseNum(iNo):
    iDigit = 0

    while(iNo != 0):
        iDigit = iNo % 10
        print(iDigit,end="")
        iNo = iNo // 10

def main():

    iValue = 0

    print("Enter the number : ",end="")
    iValue = int(input())

    ReverseNum(iValue)
    
if __name__ == "__main__":
    main()