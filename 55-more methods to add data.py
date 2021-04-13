#insert method
# how to join(concatenate) two lists
# extend method
# difference between append and extend method

fruits1=['mango','orange']
# fruits1.insert(1,"grapes") #insert method is used to insert data by passing index
# print(fruits1)

fruits2 = ['grapes','apple']
# fruits = fruits1+fruits2 #for joining two strings we use + operator and called as concatenation
# print(fruits)

# fruits1.append(fruits2)
fruits1.extend(fruits2)#extend is used to join list in one line
print(fruits1)
print(fruits2)


