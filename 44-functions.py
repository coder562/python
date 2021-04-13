#functions are used to avoid re-write of code
# name = "vaishali"
# print(len(name)) #len-pre-defined function

#for defining fun. we use def keyword
def add_two(a,b): #function takes input
    return a+b #gives 2 numbers sum
# total = add_two(5,4) #function calling
# print(total)
print(add_two(5,4))

# user input
def add_two(a,b): #function takes input
    return a+b #gives 2 numbers sum

a=int(input("enter first number:"))
b=int(input("enter second number:"))
total = add_two(a,b)
print(total)

# for string concatenation
first_name = input("enter name")
second_name = input("enter name")
print(add_two(first_name,second_name))

