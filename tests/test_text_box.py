from conftest import browser
import time
from pages.text_box import TextBox


def test_text_box(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.user_name.send_keys("test")
    text_box.current_address.send_keys("test test test")
    text_box.submit_btn.click_force()
    time.sleep(2)
    assert text_box.name_2.exist()
    assert text_box.current_address.exist()

