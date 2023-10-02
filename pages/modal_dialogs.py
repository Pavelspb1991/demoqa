from pages.base_page import BasePage
from components.components import WebElement


class ModalDialogs(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'

        super().__init__(driver, self.base_url)

        self.modal = WebElement(driver, "div:nth-child(3) > div > ul > li")
        self.icon = WebElement(driver, "#app > header > a")
        self.smallmodal_btn = WebElement(driver, "#showSmallModal")
        self.largemodall_btn = WebElement(driver, "#showLargeModal")
        self.closeSmallModal = WebElement(driver, "#closeSmallModal")
        self.smallmodall = WebElement(driver, "body > div.fade.modal.show > div > div")
        self.largemodall = WebElement(driver, "body > div.fade.modal.show > div > div")
        self.closeLargeModall = WebElement(driver, "#closeLargeModal")




