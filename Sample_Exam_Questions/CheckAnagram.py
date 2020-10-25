def check_anagram(word1, word2):
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] != word2[-(i+1)]:
                return False
        return True
    else:
        return False


print(check_anagram("maria", "airan"))
print(check_anagram("maria", "air"))
print(check_anagram("maria", "airam"))