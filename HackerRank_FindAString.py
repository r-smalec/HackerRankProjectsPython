def count_substring1(string, sub_string):
    count = 0
    subIndex = 0
    searchString = True
    pos = 0
    while searchString:
        subIndex = string.find(sub_string, subIndex + pos)
        if subIndex < 0:
            searchString = False
        else:
            pos = 1
            count += 1
    return count

def count_substring2(string, sub_string):
    count = 0
    if string == 0 or sub_string == 0:
        return -1
    else:
        pass

    for character in range(0, ( len(string) - len(sub_string) + 1 )):
        for sub_character in range(0, len(sub_string)):
            if string[character + sub_character] == sub_string[sub_character]:
                if sub_character == len(sub_string) - 1:
                    count += 1
                pass
            else:
                break
    return count

if __name__ == '__main__':
    string = input().strip() #.strip() removes whitespaces
    sub_string = input().strip()
    
    count = count_substring1(string, sub_string)
    print(count)
    count = count_substring2(string, sub_string)
    print(count)