__author__ = 's7a'

#All imports
from extras import Logger
from corpus import Parser

# Define all constants
CORPUS_DIR = "corpus"
OUTPUT_DIR = "out"
STATS_FILE = "stats.csv"


# The main method
def main():
    Logger.log_message("Starting NCERT Readability application")

    # Run the parser
    parser = Parser(CORPUS_DIR, OUTPUT_DIR, STATS_FILE)
    parser.run()

    Logger.log_success("Application exited successfully")

# Run the main method
if __name__ == '__main__':
    main()
