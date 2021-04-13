#strings
# collection of characters inside single quotes or double quotes

first_name="vaishali"
last_name="jain"
full_name=first_name + " " +  last_name
print(full_name)

# this cant be done
TypeError: can only concatenate str (not "int") to str
print(first_name + 3)

# this can be done
print(first_name + "3")

# can also write this
print(first_name + str(3))

print(first_name * 3)