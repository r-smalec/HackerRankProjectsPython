"""
insert i e: Insert integer at position
print: Print the list.
remove e: Delete the first occurrence of integer
append e: Insert integer at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
"""

if __name__ == '__main__':
    N = int(input())
    _list = list()
    for _ in range(N):
        cmdName, *line = input().split()
        cmdArgs = list(map(int, line))
        #print(str(cmdName) + str(cmdArgs))
        if str(cmdName) == "insert":
            try:
                _list.insert(cmdArgs[0], cmdArgs[1])
            except:
                pass
        elif str(cmdName) == "print":
            print(_list)
        elif str(cmdName) == "remove":
            try:
                del _list[_list.index(cmdArgs[0])]
            except:
                pass
        elif str(cmdName) == "append":
            try:
                _list.append(cmdArgs[0])
            except:
                pass
        elif str(cmdName) == "sort":
            _list.sort()
        elif str(cmdName) == "pop":
                _list.pop(len(_list) - 1)
        elif str(cmdName) == "reverse":
            _list.reverse()
        else:
            pass
