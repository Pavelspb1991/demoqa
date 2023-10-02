from conftest import browser
from pages.webtables import Webtables
import time


def test_sort(browser):

    webtable = Webtables(browser)
    webtable.visit()
    for element in webtable.header_resize.find_elements():
        time.sleep(1)
        element.click()
        assert element.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
        time.sleep(1)

    time.sleep(1)


