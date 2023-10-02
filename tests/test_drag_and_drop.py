from conftest import browser
from pages.droppable import Droppable
import time
from selenium.webdriver import ActionChains


def test_drag_and_drop(browser):
    droppable = Droppable(browser)
    action_chains = ActionChains(browser)
    droppable.visit()

    assert droppable.drop.check_css("backgroundColor", "rgba(0, 0, 0, 0)")
    action_chains.drag_and_drop(droppable.drag.find_element(),
                                droppable.drop.find_element()
                                ).perform()
    time.sleep(1)
    assert droppable.drop.check_css("backgroundColor", "rgba(70, 130, 180, 1)")

    action_chains.drag_and_drop_by_offset(droppable.drag.find_element(), 200, 300).perform()
    time.sleep(2)

    assert droppable.drop.check_css("background-color", "rgba(70, 130, 180, 1)")
