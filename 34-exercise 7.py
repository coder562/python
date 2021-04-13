#ask user input a number containing more than one digit
# example-1256
# calculte 1+2+5+6 and print
number =input("enter a number")
#1256 #length = 4 ,last index = 3
total = 0
i=1 
while i < len(number):
    total = total + int(number[i])
    i = i + 1
print(total) 


