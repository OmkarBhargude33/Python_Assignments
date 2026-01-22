# write a program which accepts one character and print its factors
# I/P :- 12
# O/P :- 1 2 3 4 6 12

def DisplayFactors(iNo):
    if(iNo <= 0):
        print("Wrong input")
        return

    for i in range(1,iNo+1):
        if(iNo % i == 0):
            print(i)
    
def main():

    iValue = 0

    print("Enter a number : ",end="")
    iValue = int(input())

    DisplayFactors(iValue)

if __name__ == "__main__":
    main()