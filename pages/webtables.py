from pages.base_page import BasePage
from components.components import WebElement


class Webtables(BasePage):
    def __init__(self, driver):
        self.base_url = "https://demoqa.com/webtables"
        super().__init__(driver, self.base_url)

        self.add_button = WebElement(driver, "#addNewRecordButton")
        self.window = WebElement(driver, "body > div.fade.modal.show > div > div")
        self.submit_button = WebElement(driver, "#submit")
        self.first_name = WebElement(driver, "#firstName")
        self.last_name = WebElement(driver, "#lastName")
        self.email = WebElement(driver, "#userEmail")
        self.age = WebElement(driver, "#age")
        self.salary = WebElement(driver, "#salary")
        self.department = WebElement(driver, "#department")
        self.no_rows_found = WebElement(driver, "div.rt-noData")
        self.record = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(3) > div")
        self.delete_button = WebElement(driver, "span[title='Delete']")
        self.edit_record_button = WebElement(driver, "#edit-record-1")
        self.delete_button_2 = WebElement(driver, "#delete-record-1")
        self.next_button = WebElement(driver, "div.-next > button")
        self.previous_button = WebElement(driver, "div.-previous > button")
        self.row_button = WebElement(driver, " span.select-wrap.-pageSizeOptions > select")
        self.row_5_button = WebElement(driver, "#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select > option:nth-child(1)")
        self.total_pages = WebElement(driver, "div.-center > span.-pageInfo")
        self.input_number = WebElement(driver, " input[type=number]")
        self.header_resize = WebElement(driver, "div > div.rt-th.rt-resizable-header")

  # div > div.rt-th.rt-resizable-header
