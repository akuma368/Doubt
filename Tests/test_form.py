import pytest
from Pages.ProjectPage import ProjectPage
from Pages.FormPage import FormPage
from Tests.test_basic import Basic_test
from Config.config import TestData
from Pages.LoginPage import LoginPage



class TestForm(Basic_test):

    def test_title_Page(self):
        self.projectpage = ProjectPage(self.driver)
        self.loginpage= LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME,TestData.EMAIL)
        self.formpage = self.projectpage.goto_form_page()
        title_driver_gettitle = self.formpage.get_page_title(TestData.TITELE_ANGULAR)
        assert title_driver_gettitle == TestData.TITELE_ANGULAR

    def test_file_form(self):
        self.projectpage = ProjectPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.EMAIL)
        self.formpage = self.projectpage.goto_form_page()
        self.formpage.submitForm()
        flag = self.formpage.getSuccessMessage().text
        assert flag

    def test_read_success_message(self):
        self.projectpage = ProjectPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.EMAIL)
        self.formpage = self.projectpage.goto_form_page()
        self.formpage.submitForm()
        assert "success" in self.formpage.readSuccessMessage().text
