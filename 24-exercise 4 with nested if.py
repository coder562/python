#NUMBER GUESSING GAME
#make a variable like winning number and assign any number to it
#ask user to guess a number
#if user guessed correctly then print "YOU WIN !!!!"
# IF USER DIDN'T GUESSED CORRECTLY then:
    # if user guessed lower than actual number then print "too low"
    # if user guessed higher than actual number then print "too high"
#ggogle "how to generate random number in python" to generate random
# winning number


#nested if else
winning_number=27
user_input = input("guess a number b/w 1 and 100:")
user_input = int(user_input)
if user_input == winning_number:
    print("YOU WIN !!!")
else:
    if user_input < winning_number:
        print("too low")
    else:
        print("too high")

