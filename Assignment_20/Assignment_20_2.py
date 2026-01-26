import threading

def EvenFactor(iNo):
    iSum = 0
    for i in range(1,iNo+1):
        if(iNo % i == 0):
            if(i % 2 == 0):
                iSum = iSum + i

    print("Summation of Even Factors are : ",iSum)


def OddFactor(iNo):
    iSum = 0
    for i in range(1,iNo+1):
        if(iNo % i == 0):
            if(i % 2 != 0):
                iSum = iSum + i
                
    print("Summation of Odd Factors are : ",iSum)


def main():

    print("Enter a number for EvenThread :- ",end="")
    Tar1 = int(input())

    print("Enter a number for OddThread :- ",end="")
    Tar2 = int(input())

    evenThread = threading.Thread(target=EvenFactor,args=(Tar1,))
    evenThread.start()

    oddThread = threading.Thread(target=OddFactor,args=(Tar2,))
    oddThread.start()

    evenThread.join()
    oddThread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()