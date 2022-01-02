def transformSentence(sentence):
    # Write your code here
    sentenceLocal = list(sentence)
    sentence = list(sentence)

    if len(sentence) <= 1:
        return -1
    for characterPos in range(1, len(sentence)):
        character = str(sentenceLocal[characterPos])
        characterBack = str(sentenceLocal[characterPos - 1])

        if character.isalpha() and characterBack.isalpha():
            if character.lower() > characterBack.lower():
                sentence[characterPos] = character.upper()
                print(character + " > " + characterBack + " -> " + sentence[characterPos])
            elif character.lower() < characterBack.lower():
                sentence[characterPos] = character.lower()
                print(character + " < " + characterBack + " -> " + sentence[characterPos])
            else:
                print(character + " = " + characterBack)
        else:
            pass
    
    return "".join(sentence)

print(transformSentence("ab cB GG"))