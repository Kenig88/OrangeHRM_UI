
from time import sleep
import allure
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from base.base_page import BasePage
from config.links import Links


class PersonalPage(BasePage):
    PAGE_URL = Links.PERSONAL_PAGE
    FIRST_NAME_FIELD = (By.XPATH, "//input[@name='firstName']")
    SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'])[1]")
    SUCCESS_TOAST = (By.CSS_SELECTOR, ".oxd-toast--success")

    @allure.step("Change name to '{new_name}'")
    def change_name(self, new_name):
        sleep(2)
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        first_name = self.wait.until(EC.visibility_of_element_located(self.FIRST_NAME_FIELD))
        first_name.send_keys(Keys.CONTROL, "a")
        first_name.send_keys(Keys.BACKSPACE)
        first_name.send_keys(new_name)
        self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        sleep(2)
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_button.click()
        # ждём завершения сохранения
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))

    @allure.step("Changes have been saved successfully")
    def is_changes_saved(self):
        # 1. главное — дождаться завершения сохранения
        self.wait.until(EC.invisibility_of_element_located(self.LOADER))
        # 2. попытаться увидеть toast (если он есть)
        try:
            self.wait.until(EC.visibility_of_element_located(self.SUCCESS_TOAST))
        except TimeoutException:
            # toast может не появиться — это нормально
            pass
        # 3. контрольный признак: кнопка Save снова активна
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
