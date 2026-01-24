# write a lambda function using reduce() which accepts a list of number and returns product of elements

from functools import reduce

Product = lambda No1,No2 : No1 * No2

def main():
    data = []
    Len = 0

    print("Enter the length of list : ",end="")
    Len = int(input())
    
    print("Enter the data in list : ")
    for i in range(Len):
        No = int(input())
        data.append(No)

    Ret = reduce(Product,data)

    print("Product of elements are : ",Ret)

if __name__ == "__main__":
    main()