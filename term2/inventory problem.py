#inventory problem
print ("maximum of four items at once")
item1=input("please input item one  ")
item2=input("please input item two  ")
item3=input("please input item three  ")
item4=input("please input item four  ")
def exists (item1,item2,item3,item4):
    if item1 or item2 or item3 or item4=="shield":
        return x==1
    if item1 or item2 or item3 or item4=="potion":
        return y==1
    if item1 or item2 or item3 or item4=="charm":
        return z==1
    if item1 or item2 or item3 or item4=="bow":
        return a==1
if (x+y+z+a)==4:
    print("good to proceed")
else:
    print("not good to proceed")