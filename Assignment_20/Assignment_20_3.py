import threading

def EvenList(eData):
    iSum = 0
    for i in eData:
        if i % 2 == 0:
            iSum = iSum + i

    print("Summation of Even elements are : ",iSum)


def OddList(oData):
    iSum = 0
    for i in oData:
        if i % 2 != 0:
            iSum = iSum + i
                
    print("Summation of Odd Elements are : ",iSum)


def main():

    data = [2,5,8,11,14,17,1,3,5,8,10,13]

    evenThread = threading.Thread(target=EvenList,args=(data,))
    evenThread.start()

    oddThread = threading.Thread(target=OddList,args=(data,))

    evenThread.join()
    oddThread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()