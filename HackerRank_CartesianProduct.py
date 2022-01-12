from itertools import product

if __name__ == '__main__':
    #s1 = set(str(input()).replace(' ', ''))
    s1 = set(input().split())
    s1 = list(sorted(map(int, s1)))
    s2 = set(input().split())
    s2 = list(sorted(map(int, s2)))

    assert 0 < len(s1) < 30, "Length should less or equal than 30"
    assert 0 < len(s2) < 30, "Length should less or equal than 30"
    
    print("A x B = [", end = '')
    prod = ''
    for i in product(s1, s2):
        prod += str(i)
        prod += ', '
    
    print(str(prod[:-2]) + ']')
