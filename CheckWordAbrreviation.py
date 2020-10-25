def check_word_abbr(word, abbr):
    digit_pos = []
    i = 0
    j = 0
    while j < len(abbr):
        if abbr[j].isdigit():
            z = j + 1
            while z < len(abbr) and abbr[z].isdigit():
                z += 1
            i += int(abbr[j:z])
            j = z
        else:
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                return False
    if i == len(word):
        return True
    return False


print(check_word_abbr("words", "1o2s"))
print(check_word_abbr("words", "3ds"))
print(check_word_abbr("words", "5"))
print(check_word_abbr("words", "w1r2"))
print(check_word_abbr("words", "w1r3"))
print(check_word_abbr("words", "w3"))
