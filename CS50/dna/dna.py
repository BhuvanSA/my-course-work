import csv
import sys


def main():

    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print("Usage: python dna.py data.csv sequence.txt")
        exit(1)

    # TODO: Read database file into a variable
    list = []
    with open(sys.argv[1]) as db:
        dbreader = csv.reader(db)
        for line in dbreader:
            list.append(line)

    # TODO: Read DNA sequence file into a variable
    with open(sys.argv[2]) as dnaseq:
        seqreader = dnaseq.read()

    # TODO: Find longest match of each STR in DNA sequence
    list2 = []
    for x in range(0, len(list[0]), 1):
        stri = list[0][x]
        long = longest_match(seqreader, stri)
        list2.append(str(long))

    # TODO: Check database for matching profiles
    count = 0
    for x in range(1, len(list), 1):
        for y in range(1, len(list[0]), 1):
            if list[x][y] == list2[y]:
                count += 1
        if count == len(list2) - 1:
            print(list[x][0])
            return
        count = 0
    print("No match")
    return


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
