from pages.slider import Slider
import time
from selenium.webdriver import ActionChains


def test_slider(browser):
    sliderr = Slider(browser)
    sliderr.visit()
    assert sliderr.slider.exist()
    assert sliderr.slider_value.exist()
    assert sliderr.slider_long.get_dom_attribute("value") == "25"
    action_chains = ActionChains(browser)
    action_chains.drag_and_drop_by_offset(sliderr.slider_long.find_element(), 2, 0).perform()
    assert sliderr.slider_long.get_dom_attribute("value") == "50"
    time.sleep(1)



