from pages.base_page import BasePage
from components.components import WebElement


class Checkboxpage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/checkbox'
        super().__init__(driver, self.base_url)
        self.check_box = WebElement(driver, "span.rct-text")
        self.check_box_1 = WebElement(driver, ".rct-option-expand-all")
