# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    n = int(input())
    nList = set(input().split())
    b = int(input())
    bList = set(input().split())
    print(len(nList.intersection(bList)))
    print(len(nList.difference(bList)))
    print(len(nList.symmetric_difference(bList)))