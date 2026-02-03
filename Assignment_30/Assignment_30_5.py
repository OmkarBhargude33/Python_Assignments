import os
import sys

def CountFreq(Fname,search):

    try:

        Ret = os.path.exists(Fname)

        if(Ret == False):
            print("There is no such file")
            return

        fobj = open(Fname,"r")
        Buffer = fobj.read()

        Buffer = Buffer.split()

        Bflag = False

        for i in Buffer:
            if(i == search):
                Bflag = True
                break

        if(Bflag == True):
            print(f"{search} word is present in file")
        else:
            print(f"{search} word is not present in file")    
    except:
        print("File not found")

def main():
    
    if(len(sys.argv) == 3):
        CountFreq(sys.argv[1],sys.argv[2])
    else:
        print("Wrong number of input")

if __name__ == "__main__":
    main()