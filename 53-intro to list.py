#list-->ordered collection of items
# you can store anything in lists int,float,string
# we create our list using square brackets
numbers = [1,2,3,4] #simple list
print(numbers)

words=["word1","word2"] #single and double quotes are both allowed
print(words)

# mixed list
mixed = [1,2,3,4,"five","six",2.3,None]
print(mixed)

# to access the particular value in the list
numbers = [1,2,3,4] #simple list
print(numbers[1])

#to fetch first two elemnts of the list
words=["word1","word2","word3","word4"] #single and double quotes are both allowed
print(words[:2]) #slicing

#to print last element of list
mixed = [1,2,3,4,"five","six",2.3,None]
print(mixed[-1])

#to change data of a list element
mixed = [1,2,3,4,"five","six",2.3,None]
print(mixed[-1])

mixed[1] = 'two'
print(mixed)

#to replace after first index
mixed = [1,2,3,4,"five","six",2.3,None]
print(mixed[-1])

mixed[1:] = ['two','three']
print(mixed)