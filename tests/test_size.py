from conftest import browser
from pages.demoqa import DemoQA
import time
from pages.elements_page import ElementsPage

def test_size(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)


def test_visible_nav_bar(browser):
    element_page = ElementsPage(browser)
    element_page.visit()
    browser.set_window_size(400, 716)
    time.sleep(3)
    assert element_page.div_nav.visible()
    browser.set_window_size(1000, 1000)
    assert not element_page.div_nav.visible()
    
