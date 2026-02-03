import os
import sys

def CopyContent(fname,NewFile):

    Ret = os.path.isfile(fname)

    if(Ret == False):
        print("It is not file")
        return
    
    fobj = open(fname,"r")

    nobj = open(NewFile,"w")

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        nobj.write(Buffer)

        Buffer = fobj.read(1024)

    print("Data gets successfully writen in ",NewFile)

def main():
    
    if(len(sys.argv) == 3):
        CopyContent(sys.argv[1],sys.argv[2])
    else:
        print("Wrong number of input")

if __name__ == "__main__":
    main()