def is_abeccedarian(s):
    index=0
    while index < len(s)-1:
        if s[index+1] < s[index]:
            return False
        index = index+1
    return True


print(is_abeccedarian("abcd"))
print(is_abeccedarian("zwabs"))
