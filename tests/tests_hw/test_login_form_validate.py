from pages.form_page import FormPage
from conftest import browser
import time


def test_login_form_validate(browser):
    formpage = FormPage(browser)
    formpage.visit()
    assert formpage.first_name.get_dom_attribute("placeholder") == "First Name"
    assert formpage.last_name.get_dom_attribute("placeholder") == "Last Name"
    assert formpage.user_email.get_dom_attribute("placeholder") == "name@example.com"
    assert formpage.user_email.get_dom_attribute("pattern") == ('^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{'
                                                                '2,5})$')
    formpage.btn_submit.click_force()
    time.sleep(2)
    assert formpage.user_form.get_dom_attribute("class") == "was-validated"
