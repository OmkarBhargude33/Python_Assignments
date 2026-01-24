# write a lambda function using map() which accepts a list of number and returns a list 
# of sqaure of each number 

from UserDefinedFMR import mapX

Square = lambda No : No * No

def main():
    data = []
    Len = 0

    print("Enter the length of list : ",end="")
    Len = int(input())
    
    print("Enter the data in list : ")
    for i in range(Len):
        No = int(input())
        data.append(No)

    NewList = list(mapX(Square,data))

    print("Square of data is : ",NewList)

if __name__ == "__main__":
    main()