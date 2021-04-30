# in keyword and iteration in dictionary

user_info={
    'name':'vaishali',
    'age':24,
    'fav_movies':['coco','llol'],
    'fav_tunes':['awakening','fairy tale']
}

#check if key exist in dictionary
# if 'name' in user_info:
#     print('present')
# else:
#     print('not')

#check if value exist in dictionary---values method
# if 'vaishali' in user_info.values():
#     print('present')
# else:
#     print('not')

#loops in dictionary
for i in user_info:
    print(user_info[i]) #prints all the keys

#for values
for i in user_info.values():
    print(i) #prints all the values

# values method
# user_info_values=user_info.values()
# print(type(user_info_values))

#keys method
# user_info_keys=user_info.keys()
# print(type(user_info_keys))

# items method
# user_items = user_info.items()
# print(user_items)
# print(type(user_items))

for key, value in user_info.items():
    print(f"key is {key} and value is {value}")
    