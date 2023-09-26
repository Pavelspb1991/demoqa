from pages.base_page import BasePage
from components.components import WebElement


class KoupAdd(BasePage):
    def __init__(self, driver):
        self.base_url = 'http://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.add_element = WebElement(driver, "#content > div > button")
        self.delete_btns = WebElement(driver, "#elements > button")
