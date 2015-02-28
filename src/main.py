__author__ = 's7a'

#  All imports
from os import path
from extras import Logger
from corpus import Parser
from analyzer import Merger
from analyzer import ReadabilityCalculator

# Define all constants
CORPUS_DIR = "corpus"
OUTPUT_DIR = "out"
STATS_FILE = "stats.csv"
MERGED_STATS_FILE = "merged_stats.csv"
RESULTS_FILE = "readability_results.csv"


# The main method
def main():
    Logger.log_message("Starting NCERT Readability application")

    # Run the parser
    parser = Parser(CORPUS_DIR, OUTPUT_DIR, STATS_FILE)
    parser.run()

    # Merge the stats
    merger = Merger(path.join(OUTPUT_DIR, STATS_FILE),
                    path.join(OUTPUT_DIR, MERGED_STATS_FILE))

    merger.run()

    readability_calc = ReadabilityCalculator(path.join(OUTPUT_DIR, MERGED_STATS_FILE),
                                             path.join(OUTPUT_DIR, RESULTS_FILE))

    readability_calc.run()

    Logger.log_success("Application exited successfully")

# Run the main method
if __name__ == '__main__':
    main()
