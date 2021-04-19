from selenium.webdriver.common.by import By
from Config.config import TestData
from Pages.BasicPage import BasicPage
from Pages.FormPage import FormPage
from Pages.LoginPage import LoginPage

class ProjectPage(BasicPage):
    TEXTS = (By.XPATH, "//*[text()= 'Web Automation Students (Selenium, Protractor & Cypress) can use below links for Practice']")
    ANGULAR3 = (By.LINK_TEXT, "Automation Practise - 3")

    def __init__(self,driver):
        super().__init__(driver)
        # self.driver.get(TestData.BASE_URL)

  #  def __init__(self,driver):
   #   login = LoginPage(self.driver)
      #login.do_login(TestData.USER_NAME,TestData.EMAIL)


    def get_page_title(self,title):
        return self.get_title(title)

    def check_text(self):
        return self.get_text(self.TEXTS)

    def goto_form_page(self):
        self.do_click(self.ANGULAR3)
        formpage = FormPage(self.driver)
        return formpage


