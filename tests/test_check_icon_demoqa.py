from pages.demoqa import DemoQa
from conftest import browser


def test(browser):
    demo_page = DemoQa(browser)
    demo_page.visit()
    demo_page.click_on_the_icon()
    assert demo_page.equal_url()
    assert demo_page.exist_icon()




# def test_visit(browser):
#     browser.get("https://demoqa.com/")
#     icon = browser.find_element(By.CSS_SELECTOR, "#app > header > a")
#
#     if icon is None:
#         print("Элемент не найден")
#     else:
#         print("Элемент найден")
