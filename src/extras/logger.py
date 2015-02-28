__author__ = 's7a'


# The Logger class
class Logger:

    # Constructor for Logger
    def __init__(self):
        # Unused
        pass

    @staticmethod
    def log_message(message):
        print '\033[94m' + '-- ' + str(message) + '\033[0m'

    @staticmethod
    def log_error(message):
        print '\033[91m' + 'Error: ' + str(message) + '\033[0m'

    @staticmethod
    def log_success(message):
        print '\033[92m' + 'Success: ' + str(message) + '\033[0m'

    @staticmethod
    def log_result(message):
        print '\033[93m' + 'Result: ' + str(message) + '\033[0m'
