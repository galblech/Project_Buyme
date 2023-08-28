from selenium.webdriver.common.by import By
from base import BasePage
from json_file.Json_func import get_url
from constans import Constants

class SenderInfoPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(self, driver)
        self.driver.get(get_url()[2])

    def click_business(self):
        self.click_element(By.CSS_SELECTOR, "img[src='https://buyme.co.il/files/siteNewLogo997212.jpg?v=1685972779']")

    def set_price(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='הכנס סכום']", '80')

    def submit_price(self):
        self.click_element(By.CSS_SELECTOR, "div[class='mx-12 money-btn']")

    def sender_name(self):
        self.enter_text(By.ID, "ember1376", "עמית")

    def pick_event(self):
        self.click_element(By.CSS_SELECTOR, "span[alt='לאיזה אירוע?'")
        self.click_element(By.CSS_SELECTOR, "li[value='10']")

    def write_congrats(self):
        self.enter_text(By.CSS_SELECTOR, "textarea[data-parsley-group='voucher-greeting']", "מזל טוב")

    def upload_pic(self):
        # Change image path
        imagepath = "image/birthday-cake-transparent-background.png"
        self.enter_text(By.CSS_SELECTOR, "input[accept='image/png,image/jpeg,video/quicktime,video/mp4,.mov,.qt']", imagepath)

    def press_continue(self):
        self.click_element(By.CSS_SELECTOR, "button[gtm='המשך']")

    def pick_sms(self):
        self.click_element(By.CSS_SELECTOR, "svg[gtm='method-sms']")

    def sms_number(self):
        self.enter_text(By.ID, "sms", "0501234567")

    def giver_name(self):
        self.enter_text(By.CSS_SELECTOR, "input[placeholder='שם שולח המתנה']", Constants.FIRSTNAME)

    def assert_giver_name(self):
        giver_name_element = self.driver.find_element(By.CSS_SELECTOR, "input[placeholder='שם שולח המתנה']")
        giver_name = giver_name_element.get_attribute('value')
        assert giver_name == Constants.FIRSTNAME
