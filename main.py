from helpers.websiteParser import WebsiteParser
from helpers.argumentsParser import ArgumentParser

arguments = ArgumentParser()
website = WebsiteParser(arguments.website)

elements = website.getFiveElementsFor(arguments.tagName)
for element in elements:
    print(element.contents)


