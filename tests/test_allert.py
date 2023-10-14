from conftest import browser
import time
from pages.alerts import Alerts
import allure


@allure.feature("check attr")
@allure.story("Проверка видимости алерта")
@allure.severity(allure.severity_level.NORMAL)
def test_allert(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    assert not alert_page.alert()

    alert_page.alert_btn.click()
    time.sleep(2)
    assert alert_page.alert()
    alert_page.alert().accept()


# @allure.feature("check attr")
# @allure.story("Проверка конфирм")
# @allure.severity(allure.severity_level.BLOCKER)
# def test_alert_text(browser):
#     alert_page = Alerts(browser)
#     alert_page.visit()
#     alert_page.alert_btn.click()
#     # time.sleep(2)
#     # assert alert_page.alert().text() == "You clicked a button"



@allure.feature("check attr")
@allure.story("Проверка отмена конфирм")
@allure.severity(allure.severity_level.MINOR)
def test_confirm(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.confirm_btn.click()
    time.sleep(2)
    alert_page.alert().dismiss()
    assert alert_page.confirm_result.get_text() == "You selected Cancel"


@allure.feature("check attr")
@allure.story("Проверка промт")
@allure.severity(allure.severity_level.CRITICAL)
def test_promt(browser):
    alert_page = Alerts(browser)
    alert_page.visit()
    alert_page.promt_button.click()
    time.sleep(2)
    alert_page.alert().send_keys("Pavel")
    alert_page.alert().accept()
    assert alert_page.promt_result.get_text() == "You entered Pavel"
    time.sleep(2)
