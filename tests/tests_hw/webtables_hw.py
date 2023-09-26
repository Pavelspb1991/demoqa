from conftest import browser
from pages.webtables import Webtables
import  time

def test_webtables(browser):
    webtables = Webtables(browser)
    webtables.visit()

    assert webtables.add_button.exist()
    webtables.add_button.click()
    assert webtables.window.exist()
    webtables.submit_button.click()
    assert webtables.window.exist()
    

    time.sleep(2)
