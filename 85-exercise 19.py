# take input from user and print by using dictionary
user={}
name=input('what is your name:')
age=input('what is your age:')
fav_movies=input('your fav movies separated by,').split(',')
fav_songs=input('your fav songs separated by,').split(',')

user['name']=name
user['age']=age
user['fav_movies']=fav_movies
user['fav_songs']=fav_songs
for key,value in user.items():
    print(f"{key} : {value}")
