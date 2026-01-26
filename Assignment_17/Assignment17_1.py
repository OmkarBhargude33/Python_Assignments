import Arithematic


def main():

    iVal1 = 0
    iVal2 = 0
    Ret = None

    print("Enter first number : ",end="")
    iVal1 = int(input())

    print("Enter first number : ",end="")
    iVal2 = int(input())

    Ret = Arithematic.Add(iVal1,iVal2)
    print("Addition is : ",Ret)

    Ret = Arithematic.Sub(iVal1,iVal2)
    print("Substraction is : ",Ret)

    Ret = Arithematic.Mult(iVal1,iVal2)
    print("Multiplication is : ",Ret)

    Ret = Arithematic.Div(iVal1,iVal2)
    print("Division is : ",Ret)
if __name__ =="__main__":
    main()