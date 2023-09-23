from conftest import browser
import time
from pages.modal_dialogs import ModalDialogs


def test_navigation_modal(browser):
    modal_dialogs = ModalDialogs(browser)
    modal_dialogs.visit()
    modal_dialogs.refresh()
    modal_dialogs.icon.click()
    modal_dialogs.back()
    time.sleep(1)
    browser.set_window_size(900, 400)
    modal_dialogs.forward()
    time.sleep(1)
    assert modal_dialogs.get_url() == "https://demoqa.com/"
    assert modal_dialogs.get_title() == "DEMOQA"
    browser.set_window_size(1000, 1000)
