#teacher code problem
forename=input("Enter your forename: ")
middle_name=input("Enter your middle name: ")
surname=input("Enter your surname: ")
def shortener (phdr):
    if phdr=="":
        return "Z"
    else:
        short_text=phdr[:1]
        return short_text.upper()
print(shortener(forename), shortener(middle_name), shortener(surname))