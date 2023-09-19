from conftest import browser
from pages.demoqa import DemoQA
from pages.elements_page import ElementsPage

def test_navigation(browser):
    demo_page = DemoQA(browser)
    element_page = ElementsPage(browser)
    demo_page.visit()
    demo_page.btn_elements.click()
    element_page.refresh()
    browser.refresh()
    browser.back()
    browser.forward()
    assert element_page.equal_url()




