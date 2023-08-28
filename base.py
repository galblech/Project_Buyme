import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    # if an element is not found the allure report will save a screenshot
    # after The click and send text are function as part of the Base page model
    def find_elem(self, locator_type, locator_value):
        try:
            return self.driver.find_element(locator_type, locator_value)
        except NoSuchElementException:
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    def click_element(self, locator_type, locator_value):
        self.find_elem(locator_type, locator_value).click()

    def enter_text(self, locator_type, locator_value, text):
        self.find_elem(locator_type, locator_value).send_keys(text)
