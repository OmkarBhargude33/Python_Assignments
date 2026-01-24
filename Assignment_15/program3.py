# write a lambda function using filter() which accepts a list of number and returns a list 
# of odd number 

from UserDefinedFMR import filterX

Odd = lambda No : No % 2 != 0

def main():
    data = []
    Len = 0

    print("Enter the length of list : ",end="")
    Len = int(input())
    
    print("Enter the data in list : ")
    for i in range(Len):
        No = int(input())
        data.append(No)

    NewList = list(filterX(Odd,data))

    print("Odd number of list is : ",NewList)

if __name__ == "__main__":
    main()