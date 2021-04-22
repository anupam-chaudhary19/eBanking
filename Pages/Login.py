from selenium import webdriver
from Locators.locators import locators
import sys
sys.path.append("C:/Users/Anupam/PycharmProjects/eBanking")

class login():

    UserID_textbox_name = locators.UserID
    Password_textbox_name = locators.Pwd
    Login_button_name = locators.Loginbtn
    Reset_button_name = locators.Resetbtn

    def __init__(self, driver):
        self.driver = driver

    def enter_userid(self, un):
        #self.driver.find_element_by_name(self.UserID_textbox_name).clear()
        self.driver.find_element_by_name(self.UserID_textbox_name).send_keys(un)

    def enter_password(self, pwd):
        #self.driver.find_element_by_name(self.Password_textbox_name).clear()
        self.driver.find_element_by_name(self.Password_textbox_name).send_keys(pwd)

    def Login_btn(self):
        self.driver.find_element_by_name(self.Login_button_name).click()

    def Reset_btn(self):
        self.driver.find_element_by_name(self.Reset_button_name).click()
