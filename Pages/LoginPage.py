from selenium.webdriver.common.by import By
from Pages.ProjectPage import ProjectPage
from Config.config import TestData
from Pages.BasicPage import BasicPage


class LoginPage(BasicPage):
    NAME_ID = (By.ID, "name")
    EMAIL_ID = (By.ID, "email")
    SUBMIT_ID = (By.XPATH, "//button[@id='form-submit']")
    CHECK_BOX = (By.ID, "agreeTerms")
    TEXT = (By.XPATH, "//*[text() = 'Join now to Practice']")

    def __init__(self, driver):
        super().__init__(driver)
        #self.driver.get(TestData.BASE_URL)

    def get_title_of_page(self, title):
        return self.get_title(title)

    def is_text_visible(self):
        return self.get_text(self.TEXT)

    def is_name_visible(self):
        return self.is_visible(self.NAME_ID)

    def is_email_visible(self):
        return self.is_visible(self.EMAIL_ID)

    def is_submit_visible(self):
        return self.is_visible(self.SUBMIT_ID)

    def is_checkbox_visble(self):
        return self.is_visible(self.CHECK_BOX)

    def do_login(self, Name, Email):
        self.do_send_keys(self.NAME_ID, Name)
        self.do_send_keys(self.EMAIL_ID, Email)
        self.do_click(self.SUBMIT_ID)

    def goto_project_page(self, Name, Email):
        self.do_send_keys(self.NAME_ID, Name)
        self.do_send_keys(self.EMAIL_ID, Email)
        self.do_click(self.SUBMIT_ID)
        projectpage = ProjectPage(self.driver)
        return projectpage
