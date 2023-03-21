# Problem 1


def split_in_half(n: str):
    l = len(n)
    splitter = round((l / 2) + .1)
    str1 = n[0:splitter]
    str2 = n[splitter:]
    output = str2 + str1
    return output


# Problem 2
def unique_chars(n: str):
    l = len(n)
    for i in range(l):
        letter = n[i]
        if letter in n[i+1:]:
            return False
    return True


#Function calls
print(split_in_half('bbbbbcaaaaa'))
print(unique_chars('abcde'))
print(unique_chars('aabcde'))
print(unique_chars('abcdee'))




