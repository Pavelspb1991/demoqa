import time
from conftest import browser
from pages.elements_page import ElementsPage


def test_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)

    elements_page.visit()
    assert elements_page.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(3)
    assert not elements_page.btn_sidebar_first_checkbox.visible()

