#inventory problem
print ("maximum of four items at once")
itmI=input("please input item one  ")
itmII=input("please input item two  ")
itmIII=input("please input item three  ")
itmIV=input("please input item four  ")
def sub1 (placeholder):
    if placeholder=="bow":
        return True
    elif placeholder=="shield":
        return True
    elif placeholder=="charm":
        return True
    elif placeholder=="potion":
        return True
    else:
        return False
def sub2 (placeholderr):
    if placeholderr==True:
        return "this item is needed"
    else:
        return "this item is not needed"
print ("item one:",sub2(sub1(itmI)))
print ("item two:",sub2(sub1(itmII)))
print ("item three:",sub2(sub1(itmIII)))
print ("item four:",sub2(sub1(itmIV)))