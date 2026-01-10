#day format
def function (day):
    if day=="1":
        return "monday"
    if day=="2":
        return "tuesday"
    if day=="3":
        return "wednesday"
    if day=="4":
        return "thursday"
    if day=="5":
        return "friday"
    if day=="6":
        return "saturday"
    if day=="7":
        return "sunday"

number=input ("please input the number of day     ")
print ("the day is",function (number), "have a nice day")
