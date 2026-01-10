ammount=float(input("ammount in GBP"))
currency=input("enter currency youw wish to convert to (capital letter first)")
if currency=="Dollars":
    ammount=ammount*1.33
    print("your ammount is",ammount,currency,)
if currency=="Euro":
    ammount=ammount*1.15
    print("your ammount is",ammount,currency,)
if currency=="Yuan":
    ammount=ammount*9.49
    print("your ammount is",ammount,currency,)
if currency=="Yen":
    ammount=ammount*202.98
    print("your ammount is",ammount,currency,)    
