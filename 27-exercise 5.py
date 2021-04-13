#WATCH COCO
# ask user's name and age
# if user's name starts with ('a' or 'A') and age is above 10 then
# print 'you can watch COCO movie'
# else print 'sorry, you can't watch COCO movie

user_name=input("enter your name :")
user_age = input("enter your age :")
user_age = int(user_age)
if user_age>=10 and (user_name[0] == 'a' or user_name[0] == 'A'):
    print("you can watch COCO movie")
else:
    print("you can't watch COCO mvie")