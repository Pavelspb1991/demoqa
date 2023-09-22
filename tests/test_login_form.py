from conftest import browser
import time
from pages.form_page import FormPage
from selenium.webdriver.common.by import By


def test_login_from(browser):
    form_page = FormPage(browser)
    form_page.visit()
    form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys("tester")
    form_page.hobbies.click_force()
    form_page.current_adress.send_keys("Санкт-Петербург")
    form_page.last_name.send_keys("testerovich")
    form_page.user_email.send_keys("test@ttt.tt")
    form_page.gender_radio_1.click_force()
    time.sleep(2)
    form_page.user_number.send_keys("9992223344")
    time.sleep(2)
    form_page.state.send_keys("NCR")
    # form_page.state.enter() # для красоты  сделал таб и enter ,но можно и через два enter
    form_page.state.tab()
    time.sleep(1)
    form_page.city.send_keys("Delhi")
    form_page.city.enter()
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)
    assert form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.btn_close_modal.click_force()
