import threading

def CountSmall(str):
    print("SmallThread :ID :- ",threading.get_ident())
    data = list(str)
    iCnt = 0

    for i in data:
        if(i >= 'a' and i <= 'z'):
            iCnt = iCnt + 1
    print("Number Lowercase are : ",iCnt)

def CountCapital(str):
    print("CountThread ID:- ",threading.get_ident())
    data = list(str)
    iCnt = 0

    for i in data:
        if(i >= 'A' and i <= 'Z'):
            iCnt = iCnt + 1
    print("Number Uppercase are : ",iCnt)

def CountDigit(str):
    print("DigitThread ID :- ",threading.get_ident())
    data = list(str)
    iCnt = 0

    for i in data:
        if(i >= '0' and i <= '9'):
            iCnt = iCnt + 1

    print("Number digits are : ",iCnt)

def main():

    data = "India Is MY CoUntRy 26 01 2026"

    SmallThread = threading.Thread(target=CountSmall,args=(data,))
    SmallThread.start()

    CapitalThread = threading.Thread(target=CountCapital,args=(data,))
    CapitalThread.start()

    DigitThread = threading.Thread(target=CountDigit,args=(data,))
    DigitThread.start()

    SmallThread.join()
    CapitalThread.join()
    DigitThread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()