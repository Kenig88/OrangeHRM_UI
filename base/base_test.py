import pytest

from config.data import Data
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.personal_page import PersonalPage


@pytest.mark.usefixtures("driver")
class BaseTest:
    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup_pages(self, request, driver):
        self.driver = driver
        self.data = Data()
        self.login_page = LoginPage(driver)
        self.dashboard_page = DashboardPage(driver)
        self.personal_page = PersonalPage(driver)




# import pytest
# from selenium import webdriver
#
# from config.data import Data
# from pages.login_page import LoginPage
# from pages.dashboard_page import DashboardPage
# from pages.personal_page import PersonalPage
#
#
# class BaseTest: #в этом классе я делаю тесты мультистраничными и мне не нужно импортировать pages в них
#     data: Data
#     login_page: LoginPage
#     dashboard_page: DashboardPage
#     personal_page: PersonalPage
#
#     @pytest.fixture(autouse=True) #autouse = будет применяться автоматически для всех тестов
#     def open(self, request):
#         driver = webdriver.Chrome()
#         request.cls.driver = driver #чтобы мог использовать в тестах driver если понадобиться
#         request.cls.data = Data()
#         request.cls.login_page = LoginPage(driver)
#         request.cls.dashboard_page = DashboardPage(driver)
#         request.cls.personal_page = PersonalPage(driver)
#         yield driver
#         driver.quit()