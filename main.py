import sys
from helpers.website import Website
from helpers.arguments import ArgumentParser

args = ArgumentParser(sys.argv[1:])

newwebsite = Website(args.website)

elements = newwebsite.getFiveElements(args.tagName)
for element in elements:
    print(element)
