from conftest import browser
from pages.demoqa import DemoQA
import time


def test_size(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    browser.set_window_size(1000, 300)
    time.sleep(2)
    browser.set_window_size(1000, 1000)
