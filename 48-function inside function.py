def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
def new_greatest(a,b,c):
    bigger = new_greatest(a,b)
    return new_greatest(bigger,c)
print(new_greatest(69,89,56))