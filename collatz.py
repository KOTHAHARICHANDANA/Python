mylist = []
def getCollatzSequence(x):
    if(x < 0):
        return 
    else:
        mylist.append(x)
        while(x > 1):
            if(x % 2 == 0):
                x = x//2
                mylist.append(x)
            else:
                x = x*3 + 1
                mylist.append(x)
    return mylist
