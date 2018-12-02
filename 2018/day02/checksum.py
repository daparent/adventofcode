#!/usr/bin/python3


def checkForRepeats(line, num_repeats):
    occurences = -1
    for c in line:
        occurences = line.count(c)
        if occurences == num_repeats:
            return True


def calcChecksum(first, second):
    return first * second


def main():
    print("Finding checksum, hold on to your butts...")
    two_repeats = 0
    three_repeats = 0
    with open("input.txt", "r") as inputfile:
        for line in inputfile:
            if checkForRepeats(line, 2):
                two_repeats += 1
            if checkForRepeats(line, 3):
                three_repeats += 1
    print('Checksum is: {}'.format(calcChecksum(two_repeats, three_repeats)))

if __name__ == "__main__":
    main()
