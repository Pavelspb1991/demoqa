from conftest import browser
from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage


def test_seo(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    assert browser.get_title() == "DEMOQA"

