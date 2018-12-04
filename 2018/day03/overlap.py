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


def hasOverlap(fabric, line):
    left = getNumber(line, '@', ',')
    top = getNumber(line, ',', ':')
    width = getNumber(line, ':', 'x')
    height = getNumber(line, 'x', -1)
    for x in range(left, left + width):
        for y in range(top, top + height):
            if fabric[x][y] > 1:
                return True
    return False


def main():
    fabric = initFabric()
    amountOverlap = 0
    all_lines = []
    with open('input.txt', 'r') as inputfile:
        all_lines = inputfile.readlines()
    for line in all_lines:
        amountOverlap += checkOverlap(fabric, line)
    print('There is {} inches of overlap'.format(amountOverlap))
    claim_num = 0
    for line in all_lines:
        claim_num = getNumber(line, '#', ' ')
        if not hasOverlap(fabric, line):
            break
    print('Claim {} has no overlap'.format(claim_num))


if __name__ == "__main__":
    main()
