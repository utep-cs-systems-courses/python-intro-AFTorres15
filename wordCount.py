# Imported Libraries
import sys
import re
import string

input_file_name = sys.argv[1]
output_file_name = sys.argv[2]

# Word dictionary
dictionary = {}

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Correct usage: wordCount.py <input text file> <output file>")
        exit()

    # attempt to open input file and write in it
    with open(input_file_name, 'r') as inputFile:
        for line in inputFile:
            # Remove the leading spaces and newline character
            line = line.strip()

            # Convert the characters in line to lowercase to avoid case mismatch
            line = line.lower()

            # Remove the punctuation marks from the line
            line = line.translate(line.maketrans("", "", string.punctuation))

            # split line on whitespace and punctuation
            # word = re.split('[ \t]', line)
            for words in line:
                if words in dictionary:
                    dictionary[words] = dictionary[words]+1
                else:
                    dictionary[words] = 1
    with open(output_file_name, "w")as outputFile:
        for word in sorted(dictionary):
            outputFile.write(word+" "+str(dictionary[word])+"\n")
    outputFile.close()