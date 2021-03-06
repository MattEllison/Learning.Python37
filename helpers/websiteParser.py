from bs4 import BeautifulSoup
import requests
from models.element import Element


class WebsiteParser:
    def __init__(self, website):
        self.website = "http://" + website
        r = requests.get(self.website)
        data = r.text
        self.soup = BeautifulSoup(data,features="html.parser")

    def getFiveElementsFor(self, tagname):
        elements = list()
        for element in self.soup.find_all(tagname)[:5]:
            elements.append(Element(element, element.contents))
        return elements
