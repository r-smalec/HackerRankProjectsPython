"""
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

>>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
>>> print Counter(myList)
Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
>>>
>>> print Counter(myList).items()
[(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
>>> 
>>> print Counter(myList).keys()
[1, 2, 3, 4, 5] #shoe sizes
>>> 
>>> print Counter(myList).values()
[3, 4, 4, 2, 1] #number of shoe in sizes
"""

from collections import Counter

if __name__ == '__main__':
        
    noOfShoes = int(input())
    shoeSizes = list(map(int, input().split()))
    shoeSizes = Counter(shoeSizes)
    noOfCustomers = int(input())
    #Counter(shoeSizes).items() / .keys() / .values()
    moneySum = 0
    for customer in range(noOfCustomers):
        shoeSize, money = map(int, input().split())
        if shoeSize in shoeSizes.keys():
            moneySum += money
            shoeSizes[shoeSize] -= 1
            if shoeSizes[shoeSize] == 0:
                del shoeSizes[shoeSize]
    
    print(moneySum)