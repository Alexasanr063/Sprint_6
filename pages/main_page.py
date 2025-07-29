from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class FaqSection:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self, url="https://qa-scooter.praktikum-services.ru/"):
        self.driver.get(url)

    def is_clickable(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute("aria-disabled") == "false"

    def click_question(self, locator):
        element = self.driver.find_element(*locator)
        if element.get_attribute("aria-disabled") == "false":
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
            element.click()
        else:
            raise Exception(f"Element {locator} is disabled and cannot be clicked")

    def get_answer_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

