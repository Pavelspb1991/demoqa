import time

import pytest

from conftest import browser
from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage
from pages.alerts import Alerts
from pages.browser_tab import BrowserTab


def test_seo(browser):
    demo_page = DemoQA(browser)
    demo_page.visit()
    assert browser.get_title() == "DEMOQA"


@pytest.mark.parametrize("pages", [Alerts, DemoQA, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    page.visit()
    time.sleep(2)
    assert page.get_title() == "DEMOQA"