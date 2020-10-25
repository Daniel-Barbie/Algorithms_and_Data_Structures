def check_palindrome(word):
    if len(word)%2 == 0:
        middle = len(word)//2
        str1 = word[:middle]
        str2 = word[middle:]
        str2 = list(str2)
        str2_mir = []
        a = len(str2)-1
        while a >= 0:
            str2_mir.append(str2[a])
            a -= 1
        str2_mir = ''.join(str2_mir)
        #print(middle)
        #print(str1)
        #print(str2)
        #print(str2_mir)
        if str1 == str2_mir:
            return True
        else:
            return False

    else:
        middle = len(word)//2
        middle_char = word[middle]
        str1 = word[:middle]
        str2 = word[middle+1:]
        str2 = list(str2)
        str2_mir = []
        a = len(str2)-1
        while a >= 0:
            str2_mir.append(str2[a])
            a -= 1
        str2_mir = ''.join(str2_mir)
        #print(middle)
        #print(middle_char)
        #print(str1)
        #print(str2)
        #print(str2_mir)
        if str1 == str2_mir:
            return True
        else:
            return False


print(check_palindrome("otzo"))

print(check_palindrome("abcba"))