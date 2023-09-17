from conftest import browser
from pages.demoqa import DemoQA


def test_icon_exist(browser):
    demo_qa_page = DemoQA(browser)
    demo_qa_page.visit()
    assert demo_qa_page.icon.exist()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()




