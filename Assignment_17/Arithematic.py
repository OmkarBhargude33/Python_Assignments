def Add(iNo1,iNo2):
    Ans = iNo1 + iNo2
    return Ans

def Sub(iNo1,iNo2):
    Ans = iNo1 - iNo2
    return Ans

def Mult(iNo1,iNo2):
    Ans = iNo1 * iNo2
    return Ans

def Div(iNo1,iNo2):
    Ans = iNo1 / iNo2
    return Ans

def ChkPrime(iNo):
    bFlag = True
    for i in range(2,(iNo//2 + 1)):
        if(iNo % i == 0):
            bFlag = False
            break
        
    return bFlag