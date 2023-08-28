from selenium.webdriver.common.by import By
from base import BasePage
from json_file.Json_func import get_url

class HomePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get(get_url()[0])

    def pick_amount(self):
        self.click_element(By.CSS_SELECTOR, "span[title='סכום']")
        self.click_element(By.XPATH, "//li[@id='ember1077']")

    def pick_region(self):
        self.click_element(By.CSS_SELECTOR, "span[title='אזור']")
        self.click_element(By.XPATH, "//li/span[text()='מרכז']")

    def pick_category(self):
        self.click_element(By.CSS_SELECTOR, "span[title='קטגוריה']")
        self.click_element(By.XPATH, "//li/span[text()='גיפט קארד למתנות ליולדת וצעצועים']")

    def press_search(self):
        self.click_element(By.XPATH, "//a[@class='ember-view bm-btn no-reverse main md ember-view' and @href='https://buyme.co.il/search']")
