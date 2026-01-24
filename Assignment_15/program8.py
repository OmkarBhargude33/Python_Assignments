# write a lambda function using filter() which accepts a list of number and returns a list of
# number which divisible by both 3 and 5

from UserDefinedFMR import filterX

Divisible = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    data = []
    Len = 0

    print("Enter the length of list : ",end="")
    Len = int(input())
    
    print("Enter the data in list : ")
    for i in range(Len):
        No = int(input())
        data.append(No)

    NewList = list(filterX(Divisible,data))

    print(NewList)

if __name__ == "__main__":
    main()