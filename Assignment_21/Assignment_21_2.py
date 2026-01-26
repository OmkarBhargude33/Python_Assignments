import threading
def Maximum(Arr):
    Max = Arr[0]
    for i in range(len(Arr)):
        if(Max < Arr[i]):
            Max = Arr[i]

    print("Maximum Element from list is : ",Max)


def Minimum(Arr):
    Min = Arr[0]
    for i in range(len(Arr)):
        if(Min > Arr[i]):
            Min = Arr[i]

    print("Minimum Element from list is : ",Min)

def main():
    data = [2,5,8,11,14,17,34,13,90,82,3,89,98]

    t1 = threading.Thread(target=Maximum,args=(data,))
    t1.start()

    t2 = threading.Thread(target=Minimum,args=(data,))
    t2.start()

    t1.join()
    t2.join()

    print("End of main thread")

if __name__ == "__main__":
    main()