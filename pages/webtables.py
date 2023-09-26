from pages.base_page import BasePage
from components.components import WebElement


class Webtables(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.add_button = WebElement(driver, "#addNewRecordButton")
        self.window = WebElement(driver, "body > div.fade.modal.show > div > div")
        self.submit_button = WebElement(driver, "#submit")


