#nitrate function
def dose (nitrate):
    if nitrate>=10:
        return ("3 ")
    if 10>nitrate>2.5:
        return ("2 ")
    if 2.5>nitrate>1:
        return ("1 ")
    if 1>nitrate>0:
        return ("0.5 ")
    if 0>nitrate:
        return ("0")

ammount=float(input ("enter ammount")) 
finaldose=dose(ammount)
print ("you need",finaldose,"doses")


