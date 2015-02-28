__author__ = 's7a'

# All imports
from os import path, walk, stat, mkdir
from extras import Logger
from syllable_counter import SyllableCounter


# The parser class
class Parser:

    # Constructor for the parser class
    def __init__(self, in_dir, out_dir, out_file):
        Logger.log_message("Initializing parser")

        self.in_dir = in_dir
        self.out_file = path.join(out_dir, out_file)
        self.out_dir = out_dir

        self.separators = [".", "!", "?"]

        self.number_of_words = {}
        self.number_of_sentences = {}
        self.number_of_syllables = {}
        self.number_of_chars = {}

    # Run the parser
    def run(self):
        Logger.log_message("Parser started running")

        # Check if the input directory exists
        try:
            stat(self.in_dir)
        except:
            Logger.log_error("Input text not found")
            return

        # Create output directory if it doesn't exist
        try:
            stat(self.out_dir)
        except:
            mkdir(self.out_dir)

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:
                in_file = path.join(dir_path, file_name)
                self.parse(in_file)

        Logger.log_message("Writing results to " + self.out_file)
        self.dump_results()
        Logger.log_success("Results have been written to " + self.out_file)

    # Parse an input file
    def parse(self, in_file):

        if not in_file.endswith(".txt"):
            return

        Logger.log_message("Parsing file " + in_file)

        input_file = open(in_file)
        content = input_file.read()

        words = content.split()

        self.number_of_words[in_file] = 0
        self.number_of_sentences[in_file] = 0
        self.number_of_syllables[in_file] = 0
        self.number_of_chars[in_file] = 0

        for word in words:

            # Check if there are any separators
            for separator in self.separators:
                if separator in word:
                    self.number_of_sentences[in_file] += 1

            sanitized_word = Parser.sanitize_word(word)

            if sanitized_word == "":
                continue

            self.number_of_words[in_file] += 1
            self.number_of_chars[in_file] += len(sanitized_word)
            self.number_of_syllables[in_file] += \
                SyllableCounter.count_syllables(sanitized_word)

        input_file.close()

    # Dump the results to the output file
    def dump_results(self):

        output_file = open(self.out_file, "w")
        output_file.write("#File;Chars;Words;Syllables;Sentences\n")

        for _file in self.number_of_words:
            result = str(_file) + \
                ";" + str(self.number_of_chars[_file]) + \
                ";" + str(self.number_of_words[_file]) + \
                ";" + str(self.number_of_syllables[_file]) + \
                ";" + str(self.number_of_sentences[_file]) + "\n"

            output_file.write(result)

        output_file.close()

    # Strip the word so that only alphabets remain
    @staticmethod
    def sanitize_word(word):
        characters = "abcdefghijklmnopqrstuvwxyz"
        return ''.join([s for s in word if s in characters])
