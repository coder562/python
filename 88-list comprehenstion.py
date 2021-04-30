#list compreshension
# with the help of list comprehension we can create of list in one line

#create a list of squares from 1 to 10
# squares=[]
# for i in range(1,11):
#     squares.append(i**2)
# print(squares)

#by using list comprehension
# square2=[i**2 for i in range(1,11)]
# print(square2)

# cretate list  of negative numbers
# negative=[]
# for i in range(1,11):
#     negative.append(-i)
# print(negative)

#by list comprehension
# new_negative = [-i for i in range(1,11)]
# print(new_negative)

names = ['vaishali','rohit','mogit']
# new_list=['v','r','m']
# new_list=[]
# for name in names:
#     new_list.append(name[0])
# print(new_list)

# by list comprehension
new_list2=[name[0] for name in names]
print(new_list2)
