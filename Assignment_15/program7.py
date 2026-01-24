# write a lambda function using filter() which accepts a list of string and returns a list
# of string having length greater then 5

from UserDefinedFMR import filterX

Greater = lambda str : True if len(str) > 5 else False

def main():
    data = []
    Len = 0

    print("Enter the length of list : ",end="")
    Len = int(input())
    
    print("Enter the data in list : ")
    for i in range(Len):
        No = input()
        data.append(No)

    NewList = list(filterX(Greater,data))

    print(NewList)

if __name__ == "__main__":
    main()