# Time complexity = O(n)
def longest_substring(s):
    char_dict = {}
    count = 0
    global_max = 0
    for i in s:
        if i in char_dict.keys():
            global_max = max(global_max, count)
            char_dict = {}
            count = 0
        else:
            char_dict[i] = 1
            count += 1
    return max(global_max, count)


print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))
print(longest_substring(""))