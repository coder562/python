#intro
# Q-why we use dictionaries?
# A-because of limitations of lists,lists are not enough to reperesnt real data

# example
# user=['vaishali',20['coco','kk kkj kkk'],['awake','ghggg']]
# this list contains user name,age,fav movie,fav tunes
# you can do this but this is not a good way to do this

# Q-what are dictionaries
# A-unordered collections of data in key : value pair

# how to create dictionaries
user={'name' : 'Vaishali','age':24}
print(user)
print(type(user))

#second method to create dictionary
user1=dict(name='vaishali',age=24)
print(type(user1))

# how to acess data from dictionary
# note-there is no indexing because of unordered collections of data
# print(user['name'])
# print(user['age'])

# which type of data a dictionary can store
# anything
# numbers,string,list,dictionary
user_info={
    'name' :'vaishali',
    'age':'20',
    'fav_movies':['coco','lmao'],
    'fav_tunes':['awake','lava']
}
# print(user_info['fav_movies'])

#how to add data to empty dictionary
user_info2={}
user_info2['name']='mohit'
print(user_info2)