x=5 #global variable which is defined outside the function
def func():
    global x #to change the value of global variable we use term global
    x=7 #the variable defined inside the function are called local variables
    return x #x has only scope upto func() not in func2() x cant be used outside func() function
print(func()) #this can be print
print(x) #cant print outside of function