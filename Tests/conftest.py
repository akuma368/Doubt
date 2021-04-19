import pytest
from selenium import webdriver
from Config.config import TestData
#from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(params =['chrome'],scope= 'class')
def init_driver(request):

    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path= TestData.CHROME_EXECUTABLE_PATH)

    '''if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=ChromeDriverManager.install())

    elif request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path= TestData.FIREFOX_EXECUTABLE_PATH)'''

    web_driver.get(TestData.BASE_URL)
    web_driver.maximize_window()
    request.cls.driver = web_driver

    yield
    web_driver.close()



