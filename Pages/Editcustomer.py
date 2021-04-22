import random
from Locators.locators import locators
from Locators.Globalvariable import globalvar
import openpyxl
class Editcustomer():
    Link_Editcust_xpath = locators.Editcustomerlink
    Custid_name = locators.Edit_custid
    Submit_name = locators.Edit_submit
    Reset_name = locators.Reset
    Edit_mobilenum_name = locators.mobilenum

    def __init__(self, driver):
        self.driver = driver

    def Click_Custlink(self):
        self.driver.find_element_by_xpath(self.Link_Editcust_xpath).click()

    def Enter_custid(self):
        wb = openpyxl.load_workbook(globalvar.path1)
        sheet = wb.active
        self.driver.find_element_by_name(self.Custid_name).send_keys(sheet.cell(1, 1).value)

    def Submit(self):
        self.driver.find_element_by_name(self.Submit_name).click()

    def Reset(self):
        self.driver.find_element_by_name(self.Reset_name).click()

    def Edit_Custdetails(self):
        self.driver.find_element_by_name(self.Edit_mobilenum_name).send_keys(str(random.randint(1, 999)).zfill(9))
