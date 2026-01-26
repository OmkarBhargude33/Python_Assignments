import threading

def Prime(Arr):
    print("Prime Elements are : ")
    for i in Arr:
        Flag = True

        for j in range(2,i // 2 + 1):
            if(i % j == 0):
                Flag = False

        if(Flag == True):
            print(i)

def NonPrime(Arr):
    print("Non Prime elements are : ")
    for i in Arr:
        if i <= 1:
            continue
        
        Flag = False 
        for j in range(2,i // 2 + 1):
            if(i % j == 0):
                Flag = True

        if(Flag == True):
            print(i)

def main():
    data = [2,5,8,11,14,17]

    t1 = threading.Thread(target=Prime,args=(data,))
    t1.start()

    t2 = threading.Thread(target=NonPrime,args=(data,))
    t2.start()

    t1.join()
    t2.join()

    print("End of main thread")

if __name__ == "__main__":
    main()