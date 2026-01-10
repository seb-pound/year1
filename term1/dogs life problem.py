age=float(input("what is your dogs age  "))

def func1 (placeholder):
    if placeholder<=2:
        return placeholder*12
    else:
        return func2 (age)
def func2 (placeholderr):
    multiplier=(placeholderr-2)*6
    return 24+multiplier
print ("your dog is",func1 (age),"years old")
