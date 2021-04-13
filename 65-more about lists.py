#generate lists with range function
# something more about pop method
# index method
# pass list to a function

# numbers = list(range(1,10))
numbers=[1,2,3,4,5,6,7,8,9,10,1]
# print(numbers)

# print(numbers.pop()) #pop returns the value popped
#  print(numbers)

# print(numbers.index(1)) #by defalut search from 0th position
print(numbers.index(1,3,14)) #3-start from 3rd position and search 1 14-stop argument

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative
print(negative_list(numbers))
