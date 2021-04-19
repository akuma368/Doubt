from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.common import by
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasicPage:

    def __init__(self, driver):
        self.driver = driver


    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def move_to_an_element(self,by_locator):
        action = ActionChains(self.driver)  # Create ActionChains object by passing driver object
        firstLevelMenu = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        action.move_to_element(firstLevelMenu).perform()


    def is_visible(self,by_locator):
        element= WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def do_select(self, by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        drp = Select(element)
        return drp

    def get_text(self,by_locator):
        texts = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return texts


    def get_title(self,title):
        WebDriverWait(self.driver,10).until(EC.title_is(title)) #it will wait until the title we sent appers and then return the actual title of the page using driver.title
        return self.driver.title




