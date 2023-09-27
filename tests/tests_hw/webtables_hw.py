from conftest import browser
from pages.webtables import Webtables
import time


def test_webtables(browser):
    webtables = Webtables(browser)
    webtables.visit()

    assert webtables.add_button.exist()
    webtables.add_button.click()
    assert webtables.window.exist()
    webtables.submit_button.click()
    assert webtables.window.exist()
    webtables.first_name.send_keys("123")
    webtables.last_name.send_keys("123")
    webtables.email.send_keys("123@mail.ru")
    webtables.age.send_keys("20")
    webtables.salary.send_keys("123")
    webtables.department.send_keys("123")
    webtables.submit_button.click_force()
    assert not webtables.window.exist()
    assert webtables.record.exist()
    webtables.edit_record_button.click()
    assert webtables.window.exist()
    webtables.first_name.clear()
    webtables.first_name.send_keys("123")
    webtables.submit_button.click()
    time.sleep(2)
    webtables.delete_button_2.click_force()
    time.sleep(1)


def test_webtabl(browser):
    webtables = Webtables(browser)
    webtables.visit()
    assert webtables.record.exist()
    assert not webtables.no_rows_found.exist()

    while webtables.delete_button.exist():
        webtables.delete_button.click()

    time.sleep(2)
    assert webtables.no_rows_found.exist()





