from collections import defaultdict

def main():
    N, M = map(int, input().split())
    nDict = defaultdict(list)
    mList = list()
    for n in range(1, N + 1):
        i = str(input())
        nDict[i].append(n)

    for m in range(M):
        i = str(input())
        mList.append(i)
    
    for mElem in mList:
        if str(nDict[mElem])[1:-1]:
            print(str(nDict[mElem])[1:-1].replace(', ', ' '))
        else:
            print(-1)


if __name__ == '__main__':
    main()