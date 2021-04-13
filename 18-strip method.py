#to remove spaces we use strip method
name="   vais    hali   "
dots="............."
#to remove left side spaces we use-lstrip() method
print(name + dots)
print(name.lstrip() + dots)

#to remove left side spaces we use-rstrip() method
print(name.rstrip() + dots)
#strip method removes both left and right spaces but dont remove spaces between character like vai   jkk
print(name.strip() + dots)

#to remove all spaces like in b/w of chracters and left and right
print(name.replace(" ", "") + dots)
