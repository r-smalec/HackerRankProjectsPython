def swap_case(s):
    localText = ''
    for character in list(s):
        if str(character).isalpha():
            if str(character).islower():
                character = str(character).upper()
            elif str(character).isupper():
                character = str(character).lower()
        else:
            pass
        localText += character
    return localText

if __name__ == '__main__':
    inText = []
    inText = input()
    print(swap_case(inText))