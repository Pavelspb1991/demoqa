from conftest import browser
from pages.alerts import Alerts
import time


def test_check_alert(browser):
    alerts = Alerts(browser)
    alerts.visit()
    assert alerts.time_alert_button.exist()
    alerts.time_alert_button.click()
    time.sleep(6)
    assert alerts.alert()
    alerts.alert().accept()

