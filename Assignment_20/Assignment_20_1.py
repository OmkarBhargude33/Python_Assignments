import threading

def Even():
    print("Even Numbers : ")
    for i in range(2,21,2):
        print(i)

def Odd():
    print("Odd Numbers : ")
    for i in range(1,20,2):
        print(i)

def main():

    evenThread = threading.Thread(target=Even)
    evenThread.start()

    oddThread = threading.Thread(target=Odd)
    oddThread.start()

    evenThread.join()
    oddThread.join()

if __name__ == "__main__":
    main()