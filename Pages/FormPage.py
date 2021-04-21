from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasicPage import BasicPage


class FormPage(BasicPage):

    HOME = (By.XPATH,"//a[@href = '/angularpractice']")
    SHOP = (By.XPATH, "//a[@href = '/angularpractice/shop']")
    NAME = (By.CSS_SELECTOR , "input[name= 'name']")
    EMAIL = (By.CSS_SELECTOR, "input[name= 'email']")
    PASSWORD = (By.CSS_SELECTOR, "input[type= 'password']")
    GENDER = (By.XPATH, "//select[@id ='exampleFormControlSelect1']")
    EMPLOYEMENT = (By.XPATH, "//label[@for = 'exampleFormControlRadio1']")
    DOB= (By.XPATH, "//input[@name='bday']")
    SUBMIT = (By.XPATH, "//input[@value='Submit']")
    SUCCESSMESSAGE = (By.CSS_SELECTOR, "[class*='alert-success']")
    EMPLOYED = (By.ID, "inlineRadio2")

    def __init__(self,driver):
        super().__init__(driver)
        #self.driver.get(TestData.BASE_URL)

    def get_page_title(self,title):
        return self.get_title(title)

    def getName(self):
        return self.is_visible(self.NAME)


    def getEmail(self):
        return self.is_visible(self.EMAIL)

    def getPassword(self):
        return self.is_visible(self.PASSWORD)

    def getGender(self):
        return self.is_visible(self.GENDER)

    def getEmployement(self):
        return self.is_visible(self.EMPLOYEMENT)

    def submitForm(self):
        self.do_send_keys(self.NAME,TestData.NAME)
        self.do_send_keys(self.EMAIL,TestData.EMAILFORM)
        self.do_send_keys(self.PASSWORD,TestData.PASSWORD)
        drops= self.do_select(self.GENDER)
        drops.select_by_value("Male")
        self.do_click(self.EMPLOYED)
        self.do_send_keys(self.DOB,TestData.DOB)
        self.do_click(self.SUBMIT)

    def getSuccessMessage(self):
        return self.is_visible(self.SUCCESSMESSAGE)

    def readSuccessMessage(self):
        return self.get_text(self.SUCCESSMESSAGE)