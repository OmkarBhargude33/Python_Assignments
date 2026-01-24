# write a lambda function using reduce() which accepts a list of number and returns Maximum of element

from UserDefinedFMR import reduceX

Maximum = lambda No1,No2 : No1 if No1 > No2 else No2

def main():
    data = []
    Len = 0

    print("Enter the length of list : ",end="")
    Len = int(input())
    
    print("Enter the data in list : ")
    for i in range(Len):
        No = int(input())
        data.append(No)

    Ret = reduceX(Maximum,data)

    print("Maximum element is  : ",Ret)

if __name__ == "__main__":
    main()