from conftest import browser
from pages.elements_page import ElementsPage


def test_flex_menu(browser):
    element = ElementsPage(browser)
    element.visit()
    assert element.block_menu.check_css("flex", '0 0 25%')
    assert element.block_menu.check_css("max-width", '25%')
    browser.set_window_size(400, 716)
    assert element.block_menu.check_css("flex", '0 0 100%')
    assert element.block_menu.check_css("max-width", '100%')
    browser.set_window_size(1000, 1000)
