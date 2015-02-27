__author__ = 's7a'

# All imports
from os import path, walk, stat, mkdir
from extras import Logger


# The parser class
class Parser:

    # Constructor for the parser class
    def __init__(self, in_dir, out_file):
        Logger.log_message("Initializing parser")

        self.in_dir = in_dir
        self.out_file = out_file

        self.separators = [".", "!", "?"]

    # Run the parser
    def run(self):
        Logger.log_message("Parser started running")

        try:
            stat(self.in_dir)
        except:
            Logger.log_error("Input text not found")
            return

        for(dir_path, _, file_names) in walk(self.in_dir):
            for file_name in file_names:
                in_file = path.join(dir_path, file_name)
                self.parse(in_file)

        Logger.log_success("Results have been written to " + self.out_file)

    def parse(self, in_file):
        Logger.log_message("Parsing file " + in_file)
