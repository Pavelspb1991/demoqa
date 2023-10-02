from pages.progressbar import ProgressBar
import time
from conftest import browser


def test_progress_bar(browser):
    bar = ProgressBar(browser)
    bar.visit()
    time.sleep(2)
    bar.start_btn.click()

    while True:
        if bar.progressbar.get_dom_attribute("aria-valuenow") == "51":
            bar.start_btn.click()
            break


