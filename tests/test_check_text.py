from conftest import browser
from pages.elements_page import ElementsPage
from pages.demoqa import DemoQA


def test_page_elements(browser):
    elements_page = ElementsPage(browser)
    demo_qa_page = DemoQA(browser)

    elements_page.visit()
    assert elements_page.text.get_text() == 'Elements'
    assert elements_page.btn_sidebar_first.exist()
    assert elements_page.btn_sidebar_first_textbox.exist()

    demo_qa_page.visit()
    assert demo_qa_page.footer_text.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'
    demo_qa_page.btn_elements.click()
    assert elements_page.text_center.get_text() == 'Please select an item from left to start practice.'
