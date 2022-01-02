"""
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
"""
def print_rangoli(size):
    # your code goes here
    # chr(ord('d') - 1) -> 'c'

    half = list()
    halfShortenReversed = list()

    for line in range(0, size):
        quaterLine = list()
        quaterLineReversed = list()
        for character in range(0, size - line):
            quaterLine.append(chr(ord('a') + character + line))
            quaterLine.append('-')
        
        quaterLine.pop()
        quaterLine.append('-' * 2*line)
        quaterLineReversed = quaterLine[:0:-1]
        half.append(''.join(quaterLineReversed))
        half[len(half) - 1] += ''.join(quaterLine)
        del quaterLine
        del quaterLineReversed

    halfShortenReversed = half[:0:-1]

    ragnoli = '\n'.join(halfShortenReversed)
    if size > 1:
        ragnoli += '\n'
    ragnoli += '\n'.join(half)
    print(ragnoli)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)