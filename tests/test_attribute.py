from conftest import browser
from pages.text_box import TextBox
import allure


@allure.feature("check attr")
def test_placeholder(browser):
    text_box = TextBox(browser)
    text_box.visit()
    assert text_box.user_name.get_dom_attribute("placeholder") == "Full Name"
