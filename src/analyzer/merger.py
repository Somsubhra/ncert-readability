__author__ = 's7a'

# All imports
from extras import Logger


# Merge the results
class Merger:

    # Constructor for the merger class
    def __init__(self, in_file, out_file):
        Logger.log_message("Initializing merger")

        self.in_file = in_file
        self.out_file = out_file

        self.file_names = "abcdefghijklmnopqrstuvwxyz"

        self.number_of_chars = {}
        self.number_of_words = {}
        self.number_of_sentences = {}
        self.number_of_syllables = {}

    # Run the merger
    def run(self):
        Logger.log_message("Running merger on " + self.in_file)

        input_file = open(self.in_file)

        for line in input_file.readlines():

            if line[0] == "#":
                continue

            cols = line.split(";")
            file_name = str(cols[0].split("/")[-1])

            grade = self.file_names.index(file_name[0]) + 1

            if grade not in self.number_of_words:
                self.number_of_chars[grade] = 0
                self.number_of_words[grade] = 0
                self.number_of_syllables[grade] = 0
                self.number_of_sentences[grade] = 0

            self.number_of_chars[grade] += int(cols[1])
            self.number_of_words[grade] += int(cols[2])
            self.number_of_syllables[grade] += int(cols[3])
            self.number_of_sentences[grade] += int(cols[4])

        input_file.close()

        Logger.log_message("Writing merged results to " + self.out_file)
        self.dump_results()
        Logger.log_success("Results written to " + self.out_file)

    # Dump the results to the output file
    def dump_results(self):
        output_file = open(self.out_file, 'w')

        output_file.write("# Grade; Chars; Words; Syllables; Sentences\n")

        for grade in self.number_of_words:
            result = str(grade) + \
                ";" + str(self.number_of_chars[grade]) + \
                ";" + str(self.number_of_words[grade]) + \
                ";" + str(self.number_of_syllables[grade]) + \
                ";" + str(self.number_of_sentences[grade]) + "\n"

            output_file.write(result)

        output_file.close()
