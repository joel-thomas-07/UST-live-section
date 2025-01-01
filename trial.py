age = 23
ht = 5.8
fname = "John"
lname = "Doe"
fullname = fname + " " + lname
demarker = "*-*"
isMarried = False

print (fullname, " age is ", age, " and height is ", ht)
print(demarker*30)

print("First 3 characters from full name: ", fullname[:3])
print("From 3rd character: ", fullname[3:])
print("Between 3rd and 6th character: ", fullname[3:7])
print("Without last 2 characters: ", fullname[:-2])
print("only last two characters: ", fullname[-2:])
print("Reversed: ", fullname[::-1])
print("At position 4: ", fullname[3])
print("At 2nd last position: ",fullname[-2])
print("Number of o's: ", fullname.count('o'))

fullname = fullname.replace("John","Joan")
print("Replaced: ", fullname)
print("First o position: ", fullname.find("o"))
print("2nd o position: ", fullname.find("o", 6))
print("Split into list: ", fullname.split(" "))
print("Marital status", isMarried)