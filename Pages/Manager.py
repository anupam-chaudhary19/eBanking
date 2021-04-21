from Locators.locators import locators
class Manager():
    heading_text_xpath = locators.Heading_text

    def __init__(self, driver):
        self.driver = driver

    def Landingpage_header_verify(self):
        self.driver.find_element_by_xpath(self.heading_text_xpath).click()
