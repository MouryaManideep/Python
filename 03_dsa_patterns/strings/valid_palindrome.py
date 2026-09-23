# def ispalindrome(s1):
#     news1 = ''
#     for char in s1:
#         if char.isalnum():
#             news1 = news1 + char.lower()

#     if(news1 == news1[::-1]):
#         return True
#     else:
#         return False


# s1 = input("Enter the string: ")
# if(ispalindrome(s1)):
#         print("This is a palindrome :)")
# else:
#         print("This is not a palindrome :(")


"""Little Improvement"""
def ispalindrome(s1):
    news1 = ''
    for char in s1:
        if char.isalnum():
            news1 = news1 + char.lower()

    return news1 == news1[::-1]


s1 = input("Enter the string: ")
if(ispalindrome(s1)):
        print("This is a palindrome :)")
else:
        print("This is not a palindrome :(")


# """"""
# def is_palindrome(s):
#     # Keep only letters and digits, and convert to lowercase
#     cleaned = ''.join(char.lower() for char in s if char.isalnum())

#     # Check if it reads the same backward
#     return cleaned == cleaned[::-1]


# # Example
# s = "A man, a plan, a canal: Panama"
# print(is_palindrome(s))
