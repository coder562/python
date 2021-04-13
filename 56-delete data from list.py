fruits=['orange','apple','pear','banana','apple','kiwi']
#pop method
# fruits.pop() #deletes the last element of list if no argument is passed by default last item gets deleted
# fruits.pop(1)#deletes the given index value of item

#del
# del fruits[1] #this also delets the given index value

#remove
fruits.remove('apple') #remove is used when we dont know the index value of item but it should be present in the list otherwise error will be come out
print(fruits)#if two apples are present then only less index value apple will be deleted

#append,extend,insert(to add data)
#pop,remove,del(to delete data)