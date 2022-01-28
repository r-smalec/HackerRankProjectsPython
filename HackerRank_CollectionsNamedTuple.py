"""
>>> from collections import namedtuple
>>> Car = namedtuple('Car','Price Mileage Colour Class')
>>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
>>> print xyz
Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
>>> print xyz.Class
Y

>>> from collections import namedtuple
>>> Point = namedtuple('Point','x,y')
>>> pt1 = Point(1,2)
>>> pt2 = Point(3,4)
>>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
>>> print dot_product
11

On input:
5
ID         MARKS      NAME       CLASS     
1          97         Raymond    7         
2          50         Steven     4         
3          91         Adrian     9         
4          72         Stewart    5         
5          80         Peter      6  
"""

from collections import namedtuple

def main():
    noStudents = int(input())
    header = list()
    header = input().split()
    Students = list()
    Student = namedtuple('Student', header)
    markSum = 0
    for student in range(noStudents):
        arg1, arg2, arg3, arg4 = input().split()
        Students.append(Student(arg1, arg2, arg3, arg4))
        markSum += int(Students[student].MARKS)
    print(markSum / noStudents)

if __name__ == '__main__':
    main()