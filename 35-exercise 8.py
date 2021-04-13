#ask a user for name
#example - Vaishali Jain
#print count of each words
name = input("enter your name")
#vaishali jain
#name.count("v"),name.count(name[0]) = 1
#name.count("a"),name.count(name[1]) = 2
#name.count("i"),name.count(name[2]) = 2
#name.count("s"),name.count(name[3]) = 1
#name.count("h"),name.count(name[4]) = 1
#name.count("a"),name.count(name[5]) = 2
#name.count("l"),name.count(name[6]) = 1
#name.count("i"),name.count(name[7]) = 2

#output
# name[0] = v : 2
# a : 2 .... so on
temp_var = ""
i = 1
while i < len(name):
    if name[i] not in temp_var:
        temp_var += name[i]
        print(f"{name[i]} : {name.count(name[i])}")
    i = i+1
