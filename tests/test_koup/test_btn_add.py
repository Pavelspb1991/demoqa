import time

from conftest import browser
from pages.herokuapp import Herokuapp
from pages.KoupAdd import KoupAdd


def test_btn_add(browser):
    herokuapp = Herokuapp(browser)
    koup_add = KoupAdd(browser)

    herokuapp.visit()
    assert herokuapp.remove_elements.get_text() == "Add/Remove Elements"
    herokuapp.remove_elements.click()
    assert koup_add.equal_url()
    assert koup_add.add_element.get_text() == "Add Element"
    assert koup_add.add_element.get_dom_attribute("onclick") == "addElement()"

    koup_add.add_element.click_x(4)
    assert koup_add.delete_btns.check_count_elements(4)
    for element in koup_add.delete_btns.find_elements():
        assert element.text == "Delete"
    while koup_add.delete_btns.exist():
        koup_add.delete_btns.click()
    assert not koup_add.delete_btns.exist()
