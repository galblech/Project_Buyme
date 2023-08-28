from selenium.webdriver.common.by import By
from base import BasePage
from json_file.Json_func import get_url


class BusinessPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get(get_url()[1])

    def assert_url(self):
        url = get_url()[1]
        assert self.driver.current_url == url

    def click_business(self):
        self.click_element(By.CSS_SELECTOR, "img[src='https://buyme.co.il/files/siteNewLogo997212.jpg?v=1685972779']")

    def set_price(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", '80')

    def submit_price(self):
        self.click_element(By.CSS_SELECTOR, "div[class='mx-12 money-btn']")
