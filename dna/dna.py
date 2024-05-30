import csv
import sys


def main():

    # Check command line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    # Read the DNA database file
    dbf = sys.argv[1]
    with open(dbf, "r") as database_file:
        reader = csv.DictReader(database_file)
        database = list(reader)

    # Read the DNA sequence file
    sqf = sys.argv[2]
    with open(sqf, "r") as sequence_file:
        sequence = sequence_file.read()

    # Find the longest match of each STR in the DNA sequence
    str_counts = {}
    for key in database[0].keys():
        if key != "name":
            str_counts[key] = longest_match(sequence, key)

    # Check the database for matching profiles
    for row in database:
        if all(int(row[key]) == str_counts[key] for key in row.keys() if key != "name"):
            print(row["name"])
            return

    print("No match")


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
