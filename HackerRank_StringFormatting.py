"""
    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
"""
def print_formatted(number):
    # your code goes here
    space = len(bin(number)) - 1
    spaceBegi = space - 1

    for n in range(1, number + 1):
        octal = oct(n)[2:]
        hexadecimal = hex(n)[2:].upper()
        binary = bin(n)[2:]
        print(' '*(spaceBegi - len(str(n))) + str(n) + ' '*(space - len(octal)) + octal + ' '*(space - len(hexadecimal)) + hexadecimal + ' '*(space - len(binary)) + binary)
        width = len("{0:b}".format(number))
        print('{0:{space}d} {0:{space}o} {0:{space}X} {0:{space}b}'.format(n, space=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)