#periodic table problem
def element (symbol):
    if symbol=="H":
        return  "name:hydrogen atomic mass:1.00784 group:reactive nonmetals"
    if symbol=="He":
        return  "name:helium atomic mass:4.0026 group:noble gases"
    if symbol=="Li":
        return  "name:lithium atomic mass:6.9410  group:alkali metals"
    if symbol=="Be":
        return  "name:beryllium atomic mass:9.0122  group:alkaline earth metals"
    if symbol=="B":
        return  "name:boron atomic mass:10.811 group:metalloids"
    if symbol=="C":
        return  "name:carbon atomic mass:12.011 group:reactive nonmetals"
    

                 
        

print ("capital first letter")
letter=input ("enter symbol choose from first 6 elements    ")
print ("",element(letter),"")

                

