from bs4 import BeautifulSoup
import requests
from models.element import Element


class Website:
    def __init__(self, website):
        self.website = website
        r = requests.get("http://" + self.website)
        data = r.text
        self.soup = BeautifulSoup(data)

    def getFiveElements(self, tagname):
        elements = list()
        for link in self.soup.find_all(tagname):
            elements.append(Element(link.get('name'), link.get('value')))
        return elements[:5]
