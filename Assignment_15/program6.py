# write a lambda function using reduce() which accepts a list of number and returns Minimum of element

from functools import reduce

Minimum = lambda a,b: a if a < b else b

def main():
    data = []
    Len = 0

    print("Enter the length of list : ",end="")
    Len = int(input())
    
    print("Enter the data in list : ")
    for i in range(Len):
        No = int(input())
        data.append(No)

    Ret = reduce(Minimum,data)

    print("Minimum element is  : ",Ret)

if __name__ == "__main__":
    main()