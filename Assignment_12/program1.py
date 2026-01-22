# write a program which accepts one character and check if it is vowel
# I/P :- a
# O/P :- Vowel

def ChkVowel(cData):
    bFlag = False
    
    if(cData == 'a' or cData == 'e' or cData == 'i' or cData == 'o' or cData == 'u'):
        bFlag = True

    return bFlag
def main():

    cValue = None

    print("Enter a character : ",end="")
    cValue = input()[0]                     # used to take only one character

    bRet = ChkVowel(cValue)

    if(bRet == True):
        print(cValue,"is a vowel")
    else:
        print(cValue,"is not a vowel")

if __name__ == "__main__":
    main()