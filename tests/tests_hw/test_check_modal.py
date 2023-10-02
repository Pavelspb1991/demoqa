import pytest
from selenium import webdriver
from pages.modal_dialogs import ModalDialogs
import time


def test_check_modal(browser):
    modal = ModalDialogs(browser)

    if not modal.code_status():
        pytest.skip(reason=f"Страница {modal.base_url} недоступна")

    modal.visit()
    assert modal.smallmodal_btn.exist()
    assert modal.largemodall_btn.exist()
    modal.smallmodal_btn.click()
    assert modal.smallmodall.exist()
    time.sleep(1)
    assert modal.closeSmallModal.exist()
    modal.closeSmallModal.click()
    time.sleep(2)
    assert not modal.smallmodall.exist()
    modal.largemodall_btn.click()
    assert modal.closeLargeModall.exist()
    assert modal.smallmodall.exist()
    modal.closeLargeModall.click()
    assert not modal.smallmodall.exist()

