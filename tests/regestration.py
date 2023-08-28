from selenium.webdriver.common.by import By
from base import BasePage
from json_file.Json_func import get_url
from constans import Constants
class RegestrationPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get(get_url()[0])

    def press_log_in(self):
        self.click_element(By.CLASS_NAME, 'notSigned')

    def click_regestration(self):
        self.click_element(By.CSS_SELECTOR, "span[data-ember-action='1889']")

    def enter_f_name(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='שם פרטי']", Constants.FIRSTNAME)

    def enter_email(self):
        self.enter_text(By.CSS_SELECTOR, "input[type='email']", 'abc@123.com')

    def enter_password(self):
        self.enter_text(By.ID, 'valPass', Constants.PASSWORD)

    def re_enter_password(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='אימות סיסמה']", Constants.PASSWORD)


    def click_confirm2(self):
        self.click_element(By.CSS_SELECTOR, "span[title='סכום']")
        self.click_element(By.XPATH, "//li[@id='ember1077']")

    def click_confirm(self):
        self.click_element(By.CSS_SELECTOR, "circle[class='fill']")

    def assert_fname(self):
        first_name = self.driver.find_element(By.CSS_SELECTOR, value="input[placeholder='שם פרטי']")
        fname = first_name.get_attribute('value')
        assert fname == Constants.FIRSTNAME
