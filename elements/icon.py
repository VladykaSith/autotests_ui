from elements.base_element import BaseElement
from playwright.sync_api import expect, Locator

class Icon(BaseElement):
    @property
    def type(self)->str:
        return 'icon'