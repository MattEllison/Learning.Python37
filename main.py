from helpers.website import Website
from helpers.arguments import ArgumentParser

args = ArgumentParser()
newwebsite = Website(args.website)

elements = newwebsite.getFiveElements(args.tagName)
for element in elements:
    print(element.contents)
