#looping in tuple
# tuple with one element
# tuple without parenthesis
# tuple unpacking
# list inside tuple
# some functions that you can use with tuples

mixed=(1,2,3,4.5)

# for loop and tuple
# for i in mixed:
#     print(i)
#we can use while loop too

# tuple with one element
nums=(1,) #, is important as python detects tuple by comma
words=('word1',)
print(type(nums))
print(type(words))

# tuple without parenthesis
guitars='yamaha','baton rouge','taylor'
print(type(guitars))

# tuple unpacking
guitarists = ('maneli','jjjhhshhs','jjsjhshh')
guitarist1,guitarist2,guitarist3=(guitarists)
print(guitarist1)

# list inside tuple
favourites =('mangolia',['ujjhhh','kjjjhh'])
favourites[1].pop()
favourites[1].append("we made it")
print(favourites)

# min(),max(),sum
print(min(mixed))
print(max(mixed))
print(sum(mixed))
