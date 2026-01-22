# write a program which accepts the marks and displays grade

def DisplayGrade(iMark):

    if(iMark <= 0 or iMark > 100):
        print("Wrong input")
        return

    if(iMark < 50):
        print("FAIL")
    elif(iMark >= 50 and iMark < 60):
        print("SECOND CLASS")
    elif(iMark >= 60 and iMark < 74):
        print("FIRST CLASS")
    elif(iMark >= 75 and iMark <= 100):
        print("DISTINCTION CLASS")

def main():

    Marks = 0

    print("Enter the marks :- ",end="")
    Marks = int(input())

    DisplayGrade(Marks)

if __name__ == "__main__":
    main()