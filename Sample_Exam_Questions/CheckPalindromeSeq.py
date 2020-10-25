def check_palindrome_even(word):
    middle = len(word) // 2
    str1 = word[:middle]
    str2 = word[middle:]
    str2 = list(str2)
    str2_mir = []
    a = len(str2) - 1
    while a >= 0:
        str2_mir.append(str2[a])
        a -= 1
    str2_mir = ''.join(str2_mir)
    # print(middle)
    # print(str1)
    # print(str2)
    # print(str2_mir)
    if str1 == str2_mir:
        return True
    else:
        return False


def check_palindrome_odd(word):
    middle = len(word) // 2
    middle_char = word[middle]
    str1 = word[:middle]
    str2 = word[middle + 1:]
    str2 = list(str2)
    str2_mir = []
    a = len(str2) - 1
    while a >= 0:
        str2_mir.append(str2[a])
        a -= 1
    str2_mir = ''.join(str2_mir)
    # print(middle)
    # print(middle_char)
    # print(str1)
    # print(str2)
    # print(str2_mir)
    if str1 == str2_mir:
        return True
    else:
        return False


def check_palindrome_seq(word):
    if len(word) % 2 == 0:
        middle = len(word) // 2
        i = 1
        while middle + i <= len(word):
            sub = word[middle - i:middle + i]
            if check_palindrome_even(sub):
                print(sub)
            else:
                break
            i += 1
    else:
        middle = len(word) // 2
        middle_char = word[middle]
        i = 1
        while middle + i <= len(word):
            sub = word[middle - i:middle + i + 1]
            if check_palindrome_odd(sub) and len(sub) > 1:
                print(sub)
            else:
                break
            i += 1


print(check_palindrome_seq("abcdcba"))