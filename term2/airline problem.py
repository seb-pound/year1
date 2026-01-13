airportI=input("please input the airport you depart from  ")
airportII=input("please input the airport you arrive at  ")
def shortener (placeholder):
    short_text=placeholder[:4]
    return short_text
print (" ",shortener(airportI),"-",shortener(airportII)," ")