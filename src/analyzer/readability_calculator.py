__author__ = 's7a'

# All imports
from extras import Logger
from scipy.stats.stats import pearsonr


# The Readability Calculator class
class ReadabilityCalculator:

    # Constructor for the readability calculator
    def __init__(self, stats_file, out_file):
        Logger.log_message("Initializing Readability Calculator")

        self.stats_file = stats_file
        self.out_file = out_file

        self.readability_grade = {}

    # Run the readability calculator
    def run(self):
        Logger.log_message("Running Readability Calculator on " + self.stats_file)

        input_file = open(self.stats_file)

        for line in input_file.readlines():

            if line[0] == "#":
                continue

            cols = line.split(";")

            grade = int(cols[0])
            chars = float(cols[1])
            words = float(cols[2])
            syllables = float(cols[3])
            sentences = float(cols[4])

            flesch_kincaid_grade = 0.39 * (words / sentences) + \
                11.8 * (syllables / words) - 15.59

            self.readability_grade[grade] = flesch_kincaid_grade

        input_file.close()

        Logger.log_message("Writing results to " + self.out_file)
        self.dump_results()
        Logger.log_success("Results written to " + self.out_file)

        grades = self.readability_grade.keys()
        fk_grades = self.readability_grade.values()

        correlation = pearsonr(grades, fk_grades)
        Logger.log_result("Correlation between grade level and Flesch Kincaid grade: " \
            + str(correlation))

    # Dump the results to output file
    def dump_results(self):
        output_file = open(self.out_file, 'w')

        output_file.write("#Grade;Flesch Kincaid Grade\n")

        for grade in self.readability_grade:
            output_file.write(str(grade) + ";" + \
                str(self.readability_grade[grade]) + "\n")

        output_file.close()
