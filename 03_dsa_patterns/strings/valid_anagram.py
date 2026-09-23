def isanagram(s1, s2):
    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))

    return s1 == s2

s1 = input("Enter string : ")
s2 = input("Enter string : ")
if(isanagram(s1, s2)):
    print("This is an anagram :)")
else:
    print("This is not an anagram :(")




# """experiment"""
# a = "dcba"
# print("".join(sorted(a)))