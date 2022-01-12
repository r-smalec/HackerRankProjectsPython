def merge_the_tools(string, k):
    first = 0
    last = k
    for i in range(0, int(len(string) / k)):
        #print(string[first:last])
        s = list(string[first:last])
        ##print(sorted(set(s), key = s.index))
        print(''.join(list(sorted(set(s), key = s.index))))
        first = last
        last += k



if __name__ == '__main__':
    #string = input()
    merge_the_tools('AABCAAADA', 3)
    #merge_the_tools(string, 1)