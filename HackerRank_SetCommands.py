# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
After the first operation, (intersection_update operation), we get: set
After the second operation, (update operation), we get: set
After the third operation, (symmetric_difference_update operation), we get: set
After the fourth operation, ( difference_update operation), we get: set
The sum of elements in set after these operations is .
"""
if __name__ == "__main__":
    a = int(input())
    aSet = set(input().split())
    N = int(input())
    cmdSet = 0
    cmdArgNoSet = 0
    argSet = []
    for _ in range(N):
        cmdSet, cmdArgNoSet = input().split()
        argSet = input().split()

        if str(cmdSet) == "intersection_update":
            try:
                aSet.intersection_update(argSet)
            except:
                pass
        elif str(cmdSet) == "update":
            try:
                aSet.update(argSet)
            except:
                pass
        elif str(cmdSet) == "symmetric_difference_update":
            try:
                aSet.symmetric_difference_update(argSet)
            except:
                pass
        elif str(cmdSet) == "difference_update":
            try:
                aSet.difference_update(argSet)
            except:
                pass
        else:
            pass
    
    sumOfElements = 0
    for element in aSet:
        sumOfElements += int(element)
    print(sumOfElements)
