#!/usr/bin/python3


def initFabric():
    length = 1000
    fabric = [[0 for x in range(length)] for y in range(length)]
    return fabric


def getNumber(line, startChar, endChar):
    numStart = line.find(startChar) + 1
    numString = ''
    if endChar == -1:
        numString = line[numStart:]
    else:
        while line[numStart] == ' ':
            numStart += 1
            if numStart > len(line):
                break
        numOffset = line.find(endChar, numStart)
        numString = line[numStart:numOffset]
    return int(numString)


def checkOverlap(fabric, line):
    left = getNumber(line, '@', ',')
    top = getNumber(line, ',', ':')
    width = getNumber(line, ':', 'x')
    height = getNumber(line, 'x', -1)
    amountOverlap = 0
    for x in range(left, left + width):
        for y in range(top, top + height):
            if fabric[x][y] == 1:
                amountOverlap += 1
            fabric[x][y] += 1
    return amountOverlap


def main():
    fabric = initFabric()
    amountOverlap = 0
    with open('input.txt', 'r') as inputfile:
        for line in inputfile:
            amountOverlap += checkOverlap(fabric, line)
    print('There is {} inches of overlap'.format(amountOverlap))


if __name__ == "__main__":
    main()
