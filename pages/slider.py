from pages.base_page import BasePage
from components.components import WebElement


class Slider(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/slider"
        super().__init__(driver, self.base_url)

        self.slider_value = WebElement(driver, "#sliderValue")
        self.slider = WebElement(driver, "#sliderContainer > div.col-9 > span > div > div.range-slider__tooltip__arrow")
        self.slider_long = WebElement(driver, "#sliderContainer > div.col-9 > span > input")

