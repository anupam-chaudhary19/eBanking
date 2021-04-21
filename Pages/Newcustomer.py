import random
from selenium import webdriver
from Locators.locators import locators
import openpyxl
from Locators.Globalvariable import globalvar
import names
class Newcustomer():
    Link_newcustomer_xpath = locators.Newcustomerlink
    Textbox_custname_name = locators.custname
    Gender_radiobtn_xpath = locators.Gendermale
    Gender_radiobtn1_xpath = locators.Genderfemale
    DOB_name = locators.Dob
    Address_textbox_name = locators.Address
    City_textbox_name = locators.City
    State_textbox_name = locators.State
    Pin_textbox_name = locators.Pin
    Mobilenum_textbox_name = locators.mobilenum
    Email_textbox_name = locators.emailid
    Password_textbox_name = locators.password_txt
    Submit_btn_name = locators.submit_btn
    Reset_btn_name = locators.reset_btn
    domain = ["hotmail.com", "gmail.com", "aol.com", "mail.com", "mail.kz", "yahoo.com"]
    SuccessConfirmmessage_xpath = locators.Confirmmesg
    Custid_xpath = locators.custid

    def __init__(self, driver):
        self.driver = driver

    def Newcustomerlink(self):
        self.driver.find_element_by_xpath(self.Link_newcustomer_xpath).click()

    def Add_new_customer_name(self):
        # self.driver.find_element_by_name(self.Textbox_custname_name).clear()
        self.driver.find_element_by_name(self.Textbox_custname_name).send_keys(names.get_full_name(gender=None))

    def Add_new_customer_Gender(self):
        # self.driver.find_element_by_name(self.Textbox_custname_name).clear()
        self.driver.find_element_by_xpath(self.Gender_radiobtn_xpath).click()

    def Add_new_customer_dob(self, dob):
        self.driver.find_element_by_name(self.DOB_name).send_keys(dob)

    def Add_new_customer_address(self, ad):
        self.driver.find_element_by_name(self.Address_textbox_name).send_keys(ad)

    def Add_new_customer_city(self, cty):
        self.driver.find_element_by_name(self.City_textbox_name).send_keys(cty)

    def Add_new_customer_state(self, st):
        self.driver.find_element_by_name(self.State_textbox_name).send_keys(st)

    def Add_new_customer_pin(self, pin):
        self.driver.find_element_by_name(self.Pin_textbox_name).send_keys(pin)

    def Add_new_customer_mobnum(self, mb):
        self.driver.find_element_by_name(self.Mobilenum_textbox_name).send_keys(mb)

    def Add_new_customer_email(self, domain):
        self.driver.find_element_by_name(self.Email_textbox_name).send_keys(names.get_full_name(gender=None)+'@'+random.choice(domain))

    def Add_new_customer_password(self, pw):
        self.driver.find_element_by_name(self.Password_textbox_name).send_keys(pw)

    def Submitbtn(self):
        self.driver.find_element_by_name(self.Submit_btn_name).click()
        self.driver.find_element_by_xpath(self.SuccessConfirmmessage_xpath).click()

    def WriteCustid_toexcel(self):
        wb = openpyxl.load_workbook(globalvar.path)
        sheet = wb.active
        sheet.cell(1, 1).value = self.driver.find_element_by_xpath(self.Custid_xpath).text
        wb.save("C:\\Users\\Anupam\\Desktop\\Test_Cust.xlsx")

    def Resetbtn(self):
        self.driver.find_element_by_name(self.Reset_btn_name).click()
