import threading
iSum = 0
iMult = 1

def Sum(Arr):
    global iSum
    add = 0

    for i in Arr:
        add = add + i

    iSum = add

def Product(Arr):
    global iMult
    mul = 1
    
    for i in Arr:
        mul = mul * i

    iMult = mul

def main():
    global iSum
    global iMult

    data = [2,5,8,11,14,17,34,13,90,82,3,89,98]

    t1 = threading.Thread(target=Sum,args=(data,))
    t1.start()

    t2 = threading.Thread(target=Product,args=(data,))
    t2.start()

    t1.join()
    t2.join()

    print("Summation is : ",iSum)
    print("Product is : ",iMult)

    print("End of main thread")

if __name__ == "__main__":
    main()