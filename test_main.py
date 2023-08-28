import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as Serviceff
from tests.regestration import RegestrationPage
from tests.home_screen import HomePage
from tests.choose_business import BusinessPage
from tests.sender_info import SenderInfoPage
from json_file.Json_func import browser_type


class TestBuyMe(unittest.TestCase):

    # For each test running the Selenium Webdriver
    def setUp(self):
        browser = browser_type()
        if browser == 'chrome':
            #Change the path of webdriver
            self.driver = webdriver.Chrome(service=Service('C:\\MyPython\\Week7\\chromedriver-win32\\chromedriver-win32\\chromedriver.exe'))
        elif browser == 'firefox':
            self.driver = webdriver.Firefox(service=Serviceff('C:\\MyPython\\Week7\\geckodriver-v0.33.0-win32\\geckodriver.exe'))
        self.driver.implicitly_wait(10)

    # Testing registration to the site, I prefer not to actually register so there is no real click on register or login
    def test_1_reg_page(self):
        self.regestration_page = RegestrationPage(self.driver)
        self.regestration_page.press_log_in()
        self.regestration_page.click_regestration()
        self.regestration_page.enter_f_name()
        self.regestration_page.enter_email()
        self.regestration_page.enter_password()
        self.regestration_page.re_enter_password()
        self.regestration_page.click_confirm()
        self.regestration_page.assert_fname()

    # Using the filter search in the home screen
    def test_2_homepage_search(self):
        self.homepage_search = HomePage(self.driver)
        self.homepage_search.pick_amount()
        self.homepage_search.pick_region()
        self.homepage_search.pick_category()
        self.homepage_search.press_search()

    # Picking one of the gift options available after the search
    def test_3_choose_business(self):
        self.busniess_page = BusinessPage(self.driver)
        self.busniess_page.assert_url()
        self.busniess_page.click_business()
        self.busniess_page.set_price()
        self.busniess_page.submit_price()

    #Filling the information regarding reciver/giver
    def test_4_sender_info(self):
        self.sender_info = SenderInfoPage(self.driver)
        self.sender_info.sender_name()
        self.sender_info.pick_event()
        self.sender_info.write_congrats()
        self.sender_info.upload_pic()
        self.sender_info.press_continue()
        self.sender_info.pick_sms()
        self.sender_info.sms_number()
        self.sender_info.giver_name()
        self.sender_info.assert_giver_name()

    def tearDown(self):
        self.driver.quit()