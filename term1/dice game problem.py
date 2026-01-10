import random
dicea=random.randint(1,6)
diceb=random.randint(1,6)
dicec=random.randint(1,6)

if dicea==diceb==dicec:
    print ("your score is",dicea+diceb+dicec,)
elif dicea==diceb:
    print ("your score is",(dicea+diceb)-dicec,)
elif diceb==dicec:
    print ("your score is",(diceb+dicec)-dicea,)
elif dicec==dicea:
    print ("your score is",(dicec+dicea)-diceb,)
else:
    print ("your score is 0")

    
