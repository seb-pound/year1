#divisible problem
z=float(input("input first number   "))
y=float(input("input second number   "))

if z==0 or y==0:
    print ("false")
else:
    if (y%z)==0:
        print ("true")
    else:
        print ("false")
