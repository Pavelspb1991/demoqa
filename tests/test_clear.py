from conftest import browser
import time
from pages.text_box import TextBox


def test_clear(browser):
    text_box = TextBox(browser)
    text_box.visit()
    text_box.user_name.send_keys("Привет привет привет!")
    time.sleep(2)
    text_box.user_name.clear()
    time.sleep(2)
    assert text_box.user_name.get_text() == ""
