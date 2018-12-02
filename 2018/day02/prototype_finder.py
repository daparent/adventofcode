#!/usr/bin/python3


def findDiffsOfOne(all_lines):
    paired_lines = []
    itercnt = 0
    for line in all_lines:
        line = line.strip()
        for line2 in all_lines:
            num_diffs = 0
            line2 = line2.strip()
            if line == line2:
                continue
            itercnt += 1
            for i in range(len(line)):
                if line[i] != line2[i]:
                    num_diffs += 1
                if num_diffs > 1:
                    break
            if num_diffs <= 1:
                paired_lines.append([line, line2])
    flat_list = list(set([item for sublist in paired_lines for item in sublist]))
    return flat_list


def getCharactersThatMatch(narrowed_list):
    list_of_commons = []
    for i in range(len(narrowed_list)):
        j = i + 1
        if j >= len(narrowed_list):
            break
        common_characters = ''
        for k in range(len(narrowed_list[i])):
            if narrowed_list[i][k] == narrowed_list[j][k]:
                common_characters += narrowed_list[i][k]
        list_of_commons.append(common_characters)
    return list_of_commons


def main():
    all_lines = []
    narrowed_list = []
    with open('input.txt', 'r') as inputfile:
        all_lines = inputfile.readlines()
    narrowed_list = findDiffsOfOne(all_lines)
    print('There are {} lines with one diff'.format(len(narrowed_list)))
    print('The common characters are: {}'.format(getCharactersThatMatch(narrowed_list)))


if __name__ == "__main__":
    main()
