if __name__ == '__main__':
    scoresList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scoresList.append([name, score])
    
    minScore = min(scoresList, key = lambda x:x[1])
    #print(scoresList)
    #print(minScore)

    i = 0
    while i < len(scoresList):
        if scoresList[i][1] == minScore[1]:
            del scoresList[scoresList.index(scoresList[i])]
        else:
            i += 1

    #print(scoresList)
    minScore = min(scoresList, key = lambda x:x[1])
    secondLowestGrades = []
    for scores in scoresList:
        if scores[1] == minScore[1]:
            secondLowestGrades.append(scores)
    secondLowestGrades.sort(key = lambda x:x[0])
    #print(secondLowestGrades)
    for scores in secondLowestGrades:
        print(scores[0])