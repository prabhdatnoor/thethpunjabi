#!/usr/bin/env python3

# open original file and new file
original = open("words.csv", "r")
reversed_csv = open("reversed.csv", "w")

for line in original:
    # remove newline and whitespace
    line = line.strip()
    line = line.rstrip()

    # split line into two terms
    terms = line.split(";")

    # remove leading whitespace of second term
    terms[1] = terms[1].lstrip()

    # write terms in reverse order
    reversed_csv.write(terms[1] + ";" + terms[0] + "\n")

# close files
original.close()
reversed_csv.close()
