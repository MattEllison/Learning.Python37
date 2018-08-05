import sys
import getopt


class ArgumentParser():
    def __init__(self, argv):
        self.website = ''
        self.tagName = ''
        try:
            opts, args = getopt.getopt(argv, "w:t:", ["website=", "tagname="])
            if len(opts) != 2:
                raise Exception()
        except:
            print ('Params Required -w <website> -t <tagname>')
            sys.exit(2)

        if len(opts) != 2:
            print('no no')
            sys.exit(2)
        for opt, arg in opts:
            if opt in ("-w", "--website"):
                self.website = arg
            elif opt in ("-t", "--tagname"):
                self.tagName = arg
            else:
                print('no match')
