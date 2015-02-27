__author__ = 's7a'


# The Logger class
class Logger:

    # Constructor for Logger
    def __init__(self):
        # Unusef
        pass

    @staticmethod
    def log_message(message):
        print "-- " + str(message)

    @staticmethod
    def log_error(message):
        print "Error: " + str(message)

    @staticmethod
    def log_success(message):
        print "Success: " + str(message)

    @staticmethod
    def log_usage(message):
        print "Usage: " + str(message)
