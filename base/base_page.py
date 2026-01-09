# import allure
# from allure_commons.types import AttachmentType
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
# class BasePage:
#
#     def __init__(self, driver):
#         self.driver = driver
#         self.wait = WebDriverWait(driver, 10, poll_frequency=1)
#
#     def open(self):
#         with allure.step(f"Open {self.PAGE_URL} page"):
#             self.driver.get(self.PAGE_URL)
#
#     def is_opened(self):
#         with allure.step(f"Page {self.PAGE_URL} is opened"):
#             self.wait.until(EC.url_to_be(self.PAGE_URL))
#
#     def make_screenshot(self, screenshot_name):
#         allure.attach(
#             body=self.driver.get_screenshot_as_png(),
#             name=screenshot_name,
#             attachment_type=AttachmentType.PNG
#         )


import allure
from allure_commons.types import AttachmentType
from selenium.common import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    LOADER = ("xpath", "//div[contains(@class, 'oxd-loading-spinner')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_URL} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):  # проверяет что страница открыта
        with allure.step(f"Page {self.PAGE_URL} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))  # url_to_be - url должен быть

    # try/except не нужны, устаревшая концепция, все покрывают явные ожидания

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    def wait_loader_disappear(self):
        try:
            self.wait.until(EC.presence_of_element_located(self.LOADER))
            self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        except TimeoutException:
            pass
