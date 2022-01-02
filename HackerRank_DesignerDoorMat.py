""" 11x33
    ---------------.|.---------------
    ------------.|..|..|.------------
    ---------.|..|..|..|..|.---------
    ------.|..|..|..|..|..|..|.------
    ---.|..|..|..|..|..|..|..|..|.---
    -------------WELCOME-------------
    ---.|..|..|..|..|..|..|..|..|.---
    ------.|..|..|..|..|..|..|.------
    ---------.|..|..|..|..|.---------
    ------------.|..|..|.------------
    ---------------.|.---------------
"""

if __name__ == '__main__':
    n, m = input().split()
    n = int(n)
    m = int(m)

    doorMatHalf = list()
    for line in range(0, int((n - 1) / 2)):
        hyphens = '-' * int((m - 1) / 2 - 1 - line * 3) + '.'
        dots = '|..' * int(line)
        lineDoorMat = hyphens + dots + '|' + dots[::-1] + hyphens[::-1]
        doorMatHalf.append(lineDoorMat)
    
    doorMatInscription = 'WELCOME'
    middleDoorMatLine = '-' * int((m - len(doorMatInscription)) / 2) + doorMatInscription + '-' * int((m - len(doorMatInscription)) / 2)

    for line in doorMatHalf:
        print(line)
    print(middleDoorMatLine)
    for line in doorMatHalf[::-1]:
        print(line)