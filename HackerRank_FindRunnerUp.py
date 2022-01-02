if __name__ == '__main__':
    n = int(input())
    #arr = map(int, input().split())
    arr = list(input().split())
    #arr = list(arr)
    maxNum = max(arr)
    while maxNum in arr:
        del arr[arr.index(maxNum)]
    print(max(arr))