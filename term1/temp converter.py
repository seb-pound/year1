#temp converter problem
#ctof
def CtoF(C):
    return (c*1.8)+32
#FtoC
def FtoC(F):
    return (f-32)/1.8
#main program
c=30
F=CtoF(c)
print(c,"degrees C is",F,"degrees F")
print(F,"degrees F is",c,"degrees C")
