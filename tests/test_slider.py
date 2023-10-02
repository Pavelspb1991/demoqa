from pages.slider import Slider
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def test_slider(browser):
    sliderr = Slider(browser)
    sliderr.visit()
    assert sliderr.slider.exist()
    assert sliderr.slider_value.exist()
    time.sleep(2)

    while not sliderr.slider_value.get_dom_attribute("value") == "50":
        sliderr.slider.send_keys(Keys.ARROW_RIGHT)
    assert sliderr.slider_value.get_dom_attribute("value") == "50"
    time.sleep(1)



