from pages.base_page import BasePage
from components.components import WebElement


class RadioButton(BasePage):

    def __init__(self, driver):
        self.base_url = "https://demoqa.com/radio-button"
        super().__init__(driver, self.base_url)

        self.yes = WebElement(driver, "#yesRadio")
        self.impressive = WebElement(driver, "#impressiveRadio")
        self.no = WebElement(driver, "#noRadio")
        self.text_check = WebElement(driver, " p > span")
