def solve(s):
    s = ''.join(s)
    s = s.split(' ')
    print(s)
    for wordNo in range(0, len(s)):
        if s[wordNo].isalpha():
            s[wordNo] = s[wordNo].replace(s[wordNo][0], s[wordNo][0].upper(), 1)
    print(' '. join(s))

if __name__ == '__main__':
    s = input()
    solve(s)