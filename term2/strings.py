# surname example
# inputs: Firstname, Lastname
# outputs: first initial of Firstname Lastname all in uppercase

# Get user inputs
firstname = input("Enter Firstname: ")
lastname = input("Enter Lastname: ")

# Get the first initial and make it uppercase
initial = firstname[0].upper()

# Combine initial with lastname in uppercase
result = initial + " " + lastname.upper()

# Output the result
print(result)