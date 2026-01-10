#grade problem

def grade (ammount):
    if ammount<2:
        return "U"
    if 4>ammount>=2:
        return "1"
    if 13>ammount>=4:
        return "2"
    if 22>ammount>=13:
        return "3"
    if 31>ammount>=22:
        return "4"
    if 41>ammount>=31:
        return "5"
    if 54>ammount>=41:
        return "6"
    if 67>ammount>=54:
        return "7"
    if 80>ammount>=67:
        return "8"
    if ammount>=80:
        return "9"
def distance (grade):
    if grade(points)=="U":
        return points-2
    if grade(points)=="1":
        return points-4
    if grade(points)=="2":
        return points-13
    if grade(points)=="3":
        return points-22
    if grade(points)=="4":
        return points-31
    if grade(points)=="5":
        return points-41
    if grade(points)=="6":
        return points-54
    if grade(points)=="7":
        return points-67
    if grade(points)=="8":
        return points-80
    if grade(points)=="U":
        return nothing
        
    
points= float(input(" enter mark   "))
print ("your grade is",grade(points),"well done")
print ("you were",distance(grade),"points off the next grade, better luck next time")









    
