from conftest import browser
from pages.elements_page import ElementsPage
from pages.checkbox_page import Checkboxpage
import time

def test_find_elements(browser):
    elements_page = ElementsPage(browser)
    elements_page.visit()
    assert elements_page.btns_first_menu.check_count_elements(9)


def test_count_checkbox(browser):
    checkbox_page = Checkboxpage(browser)
    checkbox_page.visit()
    assert checkbox_page.check_box.check_count_elements(1)
    checkbox_page.check_box_1.click()
    time.sleep(2)
    assert checkbox_page.check_box.check_count_elements(17)
    checkbox_page.refresh()
    assert checkbox_page.check_box.check_count_elements(1)
