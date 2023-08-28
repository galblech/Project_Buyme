from selenium.webdriver.common.by import By
from base import BasePage


class BusinessPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get('https://buyme.co.il/search?budget=1&category=75&region=11')

    def click_business(self):
        self.click_element(By.CSS_SELECTOR, "img[src='https://buyme.co.il/files/siteNewLogo997212.jpg?v=1685972779']")

    def set_price(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", '80')

    def submit_price(self):
        self.click_element(By.CSS_SELECTOR, "div[class='mx-12 money-btn']")

    def assert_url(self):
        pass
        # url =