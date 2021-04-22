import time
from selenium import webdriver
from Locators.locators import locators
from Locators.Globalvariable import globalvar
import unittest
from Pages.Login import login
from Pages.Manager import Manager
from Pages.Newcustomer import Newcustomer
from Pages.Editcustomer import Editcustomer

class Testsuite_banking(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.driver = webdriver.Chrome(executable_path=globalvar.Chromepath)
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
# User Login
    def test_loginvalid_TC001(self):
        driver = self.driver
        driver.get(globalvar.baseURL)
        log = login(driver)
        log.enter_userid(globalvar.un)
        log.enter_password(globalvar.pwd)
        log.Login_btn()

# Landing page or Manager page
    def test_managerpage_TC002(self):
        driver = self.driver
        driver.get(globalvar.baseURL)
        log = login(driver)
        log.enter_userid(globalvar.un)
        log.enter_password(globalvar.pwd)
        log.Login_btn()
        mgr = Manager(driver)
        mgr.Landingpage_header_verify()
        pagetitle = driver.title
        if pagetitle == "Guru99 Bank Manager HomePage":
            assert True
        else:
            assert False
        time.sleep(5)

# New Customer page
    def test_Addnewcustomer_TC003(self):
        driver = self.driver
        driver.get(globalvar.baseURL)
        log = login(driver)
        log.enter_userid(globalvar.un)
        log.enter_password(globalvar.pwd)
        log.Login_btn()
        newcust = Newcustomer(driver)
        newcust.Newcustomerlink()
        newcust.Add_new_customer_name()
        newcust.Add_new_customer_Gender()
        newcust.Add_new_customer_dob(globalvar.dob)
        newcust.Add_new_customer_address(globalvar.ad)
        newcust.Add_new_customer_city(globalvar.cty)
        newcust.Add_new_customer_state(globalvar.st)
        newcust.Add_new_customer_pin(globalvar.pin)
        newcust.Add_new_customer_mobnum(globalvar.mb)
        newcust.Add_new_customer_password(globalvar.pw)
        newcust.Add_new_customer_email(globalvar.domain)
        time.sleep(10)
        newcust.Submitbtn()
        pagetitle2 = driver.title
        if pagetitle2 == "Guru99 Bank Customer Registration Page":
            assert True
        else:
            assert False
        time.sleep(5)
        newcust.WriteCustid_toexcel()
        time.sleep(10)

    def test_EditCust_TC004(self):
        driver = self.driver
        driver.get(globalvar.baseURL)
        log = login(driver)
        log.enter_userid(globalvar.un)
        log.enter_password(globalvar.pwd)
        log.Login_btn()
        edcust = Editcustomer(driver)
        time.sleep(5)
        edcust.Click_Custlink()
        edcust.Enter_custid()
        edcust.Submit()

    def tearDown(self) -> None:
        self.driver.close()
        self.driver.quit()
