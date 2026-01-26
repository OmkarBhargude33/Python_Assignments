import threading

lobj = threading.Lock()
iCnt = 0

def Update():
    global iCnt

    for _ in range(50000): 
        with lobj:                  
            iCnt = iCnt + 1         # critical section

def main():

    global iCnt
    t1 = threading.Thread(target=Update)
    t1.start()

    t2 = threading.Thread(target=Update)
    t2.start()

    t3 = threading.Thread(target=Update)
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Final value of counter is : ",iCnt)
    print("End of main thread")

if __name__ == "__main__":
    main()