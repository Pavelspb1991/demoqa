from conftest import browser
from pages.webtables import Webtables
import time


def test_webtables(browser):
    webtables = Webtables(browser)

    # предусловие

    webtables.visit()
    webtables.row_button.scroll_to_element()
    webtables.row_button.click()
    webtables.row_5_button.scroll_to_element()
    webtables.row_5_button.click()
    time.sleep(2)

    # тест-кейс

    assert webtables.next_button.get_dom_attribute("disabled")
    assert webtables.previous_button.get_dom_attribute("disabled")

    webtables.add_button.click()
    webtables.first_name.send_keys("Ivan")
    webtables.last_name.send_keys("Ivanov")
    webtables.email.send_keys("ivan@mail.ru")
    webtables.age.send_keys("20")
    webtables.salary.send_keys("100")
    webtables.department.send_keys("10")
    webtables.submit_button.click()
    webtables.add_button.click()
    webtables.first_name.send_keys("Ivan")
    webtables.last_name.send_keys("Ivanov")
    webtables.email.send_keys("ivan@mail.ru")
    webtables.age.send_keys("20")
    webtables.salary.send_keys("100")
    webtables.department.send_keys("10")
    webtables.submit_button.click()
    webtables.add_button.click()
    webtables.first_name.send_keys("Ivan")
    webtables.last_name.send_keys("Ivanov")
    webtables.email.send_keys("ivan@mail.ru")
    webtables.age.send_keys("20")
    webtables.salary.send_keys("100")
    webtables.department.send_keys("10")
    webtables.submit_button.click()
    time.sleep(2)
    assert not webtables.next_button.get_dom_attribute("disabled")  # проверка,что кнопка next доступна
    assert webtables.total_pages.get_text() == "Page of 2"
    webtables.next_button.click()
    time.sleep(1)
    assert webtables.input_number.get_dom_attribute("value") == "2"
    time.sleep(1)
    webtables.previous_button.click()
    assert webtables.input_number.get_dom_attribute("value") == "1"
