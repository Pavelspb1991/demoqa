import time
import pytest
from conftest import browser
from pages.demoqa import DemoQA
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab
from components.components import WebElement


@pytest.mark.parametrize("pages", [Alerts, DemoQA, BrowserTab])
def test_seo_meta(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.meta.exist()
    assert page.meta.get_dom_attribute("name") == "viewport"
    assert page.meta.get_dom_attribute("viewport") == "width=device-width,initial-scale=1"



