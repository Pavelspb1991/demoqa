from pages.base_page import BasePage
from components.components import WebElement


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text = WebElement(driver, '.main-header')
        self.icon = WebElement(driver, '#app > header > a')
        self.btn_sidebar_first = WebElement(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElement(driver, 'div:nth-child(1) > div > ul > #item-0 > span')
        self.text_center = WebElement(driver, 'div.col-12:nth-child(2)')
        self.btn_sidebar_first_checkbox = WebElement(driver, "div:nth-child(1) > div > ul > #item-1 > span")
        self.btns_first_menu = WebElement(driver, "div:nth-child(1) > div > ul > li")
        self.div_nav = WebElement(driver, "div > nav")
        self.block_menu = WebElement(driver, "div.row > div:nth-child(1)")
