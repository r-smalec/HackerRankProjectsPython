def isVovel(letter):
    if letter in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        return True
    else:
        return False

def minion_game(s):
    # your code goes here
    vovelsPoints = 0
    consonantsPoints = 0
    if not str(s).isalpha():
        return -1
    else:
        pass
    s = list(s)
    fullWord = ''.join(s)
    vovels = set()
    consonants = set()
    for character in s:
        if isVovel(character):
            vovels.add(character)
        else:
            consonants.add(character)        

    consonantBegWords = set()
    for consonant in consonants:
        consonantsIndexes = list()
        currIndex = 0
        while True:
            try:
                currIndex = s.index(consonant, currIndex)
                consonantsIndexes.append(currIndex)
                currIndex += 1
            except ValueError:
                break

        for consonantIndex in consonantsIndexes:
            for letterNo in range(1, len(s) + 1):
                currIndex = consonantIndex + letterNo
                try:
                    word = ''.join(s[consonantIndex:currIndex])
                except:
                    break
                consonantBegWords.add(word)

        del consonantsIndexes

    vovelBegWords = set()
    for vovel in vovels:
        vovelsIndexes = list()
        currIndex = 0
        while True:
            try:
                currIndex = s.index(vovel, currIndex)
                vovelsIndexes.append(currIndex)
                currIndex += 1
            except ValueError:
                break

        for vovelIndex in vovelsIndexes:
            for letterNo in range(1, len(s) + 1):
                currIndex = vovelIndex + letterNo
                try:
                    word = ''.join(s[vovelIndex:currIndex])
                except:
                    break
                vovelBegWords.add(word)

        del vovelsIndexes

    #print(consonantBegWords)
    for consonantWord in consonantBegWords:
        points = 0
        currIndex = 0
        while True:
            try:
                currIndex = fullWord.index(consonantWord, currIndex)
            except Exception as ex:
                #print('Exception ' + str(type(ex)))
                break
            else:
                points += 1
                currIndex += 1

        consonantsPoints += points

    #print(vovelBegWords)
    for vovelWord in vovelBegWords:
        points = 0
        currIndex = 0
        while True:
            try:
                currIndex = fullWord.index(vovelWord, currIndex)
            except Exception as ex:
                #print('Exception ' + str(type(ex)))
                break
            else:
                points += 1
                currIndex += 1

        vovelsPoints += points

    if consonantsPoints > vovelsPoints:
        print('Stuart ' + str(consonantsPoints))
        #print('Kevin ' + str(vovelsPoints))
    elif vovelsPoints > consonantsPoints:
        print('Kevin ' + str(vovelsPoints))
        #print('Stuart ' + str(consonantsPoints))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)