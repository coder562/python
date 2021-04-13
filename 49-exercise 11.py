# define is_palindrome that take one word in string as input 
# and return True if it is palindrome else return False

#palindrome - ord that reads same backwards as forwards
def is_palindrome(word):
    reversed_word=word[::-1] 
    if word == reversed_word:
        return True
    else:
        return False
print(is_palindrome("naman"))
print(is_palindrome("horse"))

#another method
# def is_palindrome(word):
    
#     if word == word[::-1]:
#         return True
#     return False
# print(is_palindrome("naman"))
# print(is_palindrome("horse"))