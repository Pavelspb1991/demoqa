import pytest

from conftest import browser
from pages.demoqa import DemoQA
from pages.radio_button import RadioButton


@pytest.mark.skip
def test_decor(browser):
    demo = DemoQA(browser)
    demo.visit()
    assert demo.h5.check_count_elements(6)

    for elem in demo.h5.find_elements():
        assert elem.text() != ''


# @pytest.mark.skipif(False, reason="просто")
def test_decor_3(browser):
    radiobutton = RadioButton(browser)

    if not radiobutton.code_status():
        pytest.skip(reason=f"Страница {radiobutton.base_url} недоступна")

    radiobutton.visit()
    radiobutton.yes.click_force()
    assert radiobutton.text_check.get_text() == "Yes"
    radiobutton.impressive.click_force()
    assert radiobutton.text_check.get_text() == "Impressive"
    assert "disabled" in radiobutton.no.get_dom_attribute("class")
