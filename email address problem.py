#email checker
email=input("please input your email address  ")
def checker (phdr):
    phdr.find("@")
    if "@" in phdr and "." in phdr:
        return "this is a valid email address"
    else:
        return "this is not a valid email address"
print (checker(email))