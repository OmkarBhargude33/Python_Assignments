#-----------------------------------#
def filterX(Task,Elements):
    Result = list()

    for i in Elements:
        Ret = Task(i)
        
        if(Ret == True):
            Result.append(i)

    return Result

#------------------------------------#
def mapX(Task, Elements):
    Result = list()

    for i in Elements:
        Ret = Task(i)
        Result.append(Ret)

    return Result

# ------------------------------------#
def reduceX(Task, Elements):
    Ret = 0

    for i in Elements:
        Ret = Task(Ret,i)

    return Ret