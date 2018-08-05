import sys
import getopt

requireArgumentsMessage = 'Params Required -w <website> -t <tag>'

class ArgumentParser():
    def __init__(self):
        argv = sys.argv[1:]
        self.website = ''
        self.tagName = ''
        try:
            opts, args = getopt.getopt(argv, "w:t:", ["website=", "tag="])
            if len(opts) != 2:
                raise Exception()
        except:
            print (requireArgumentsMessage)
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-w", "--website"):
                self.website = arg
            elif opt in ("-t", "--tag"):
                self.tagName = arg
