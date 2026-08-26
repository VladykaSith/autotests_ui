from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator

class Link(BaseElement):
    @property
    def type_of(self)->str:
        return 'link'