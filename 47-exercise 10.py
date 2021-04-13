# define a function which takes two numbers as a input and return greater of three numbers
def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print(greatest(10,70,56))