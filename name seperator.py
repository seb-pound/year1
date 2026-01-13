#name separator
name=input("Enter your full name with a space inbetween the forename and surname: ")
def separator(phdr):
    if " " not in phdr:
        return "Please enter a valid full name with a space."
    else:
        return phdr.upper().split(" ")
print(separator(name))