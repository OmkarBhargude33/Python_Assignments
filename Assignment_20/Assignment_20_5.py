import threading

lobj = threading.Lock()

def Display1(iNo):
    print("Thread1 running : ")

    for i in range(1,iNo+1):
        print(i)

def Display2(iNo):
    print("Thread2 running : ")

    for i in range(iNo,0,-1):
            print(i)


def main():


    evenThread = threading.Thread(target=Display1,args=(50,))
    evenThread.start()

    oddThread = threading.Thread(target=Display2,args=(50,))

    evenThread.join()
    oddThread.start()

    oddThread.join()

    print("Exit from main")

if __name__ == "__main__":
    main()