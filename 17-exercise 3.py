#take two comma separated inputs from user
#1.user's name,example - "harshit"
#2.a single character,"h"

#output- 2 print lines
#1.user's name length
#2.count the character that user inputed(bonus:case insensitive count)

# name,char = input("ener name and character: ").split(",")
# print(f"length of your name is {len(name)}")
# print(f"charachter count : {name.lower().count(char.lower())}") #case sensitive
#Vaishali - vaishali
#H-h

#by using strip method
#"Vaishali "------>"Vaishali"------> "vaishali"
#" H"---->"H"---->"h"
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()
name,char = input("ener name and character: ").split(",")
print(f"length of your name is {len(name)}")
print(f"charachter count : {name.strip().lower().count(char.strip().lower())}")
