#!/usr/bin/python3


def frequencyChange(cur_frequency, frequency_change):
    modifier = frequency_change[0]
    change_amount = int(frequency_change[1:])
    if modifier == '-':
        cur_frequency -= change_amount
    else:
        cur_frequency += change_amount
    return cur_frequency


def main():
    print("Calculating frequency, hold on to your butts...")
    cur_frequency = 0
    iterations = 1
    calculated_frequencies = {}
    repeated_frequency = -1
    frequency_changes = []
    with open('input.txt', 'r') as inputfile:
        frequency_changes = inputfile.readlines()
    while repeated_frequency == -1:
        for line in frequency_changes:
            cur_frequency = frequencyChange(cur_frequency, line)
            if calculated_frequencies.get(cur_frequency) is not None:
                repeated_frequency = cur_frequency
                break
            else:
                calculated_frequencies[cur_frequency] = True
        if iterations == 1:
            print("Calculated Frequency is {}".format(cur_frequency))
        iterations = iterations + 1
    print("Repeated frequncy is {}".format(repeated_frequency))


if __name__ == "__main__":
    main()
